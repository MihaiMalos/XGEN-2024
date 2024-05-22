from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
import pandas as pd
import os
import io
import csv
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
DATABASE_URL = 'test.db'
from GoogleNewsWebScraper import WebScraper
from ModelInference import RobertaInference
model_inference = RobertaInference()

@app.route('/get_datasets', methods=['GET'])
def get_datasets():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE_URL)  # Replace 'your_database_file.db' with your actual database file
        cursor = conn.cursor()

        # Query to get table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Create datasets using table names
        dataSets = [table[0] for table in tables]
        print(dataSets)
        return jsonify(dataSets)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/get_table', methods=['POST'])
def get_table():
    table_name = request.json.get('table_name')
    print(table_name)
    # Verificăm dacă table_name a fost trimis
    if not table_name:
        return jsonify({"error": "Table name not provided"}), 400

    # Conectează-te la baza de date
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Execută interogarea pentru a obține toate datele din tabel
    query = f"SELECT * FROM {table_name}"
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

    # Convertim datele tabelului într-un CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(
        io.BytesIO(csv_buffer.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'{table_name}.csv'
    )

articles = []
@app.route('/scrape_site', methods=['POST'])
def scrape_site():
    data = request.json
    website_link = data.get('siteLink')
    if not website_link:
        return jsonify({"error": "No site link provided"}), 400

    # Apelarea scraper-ului pentru a obține articolele
    global articles
    scraper = WebScraper(website_link)
    articles = scraper.extract_articles_from_page(website_link)
    article_titles = [article['title'] for article in articles]
    return jsonify(article_titles)


@app.route('/submit_articles', methods=['POST'])
def submit_articles():
    data = request.json
    selected_dataset = data.get('selectedDataSet')
    labels = data.get('labels')
    print(labels)
    global articles

    if not selected_dataset or not articles:
        return jsonify({"error": "Dataset name or articles not provided"}), 400

    con = sqlite3.connect(DATABASE_URL)
    cur = con.cursor()

    for index in range(len(articles)):
        title = articles[index].get('title')
        text = articles[index].get('text')
        source = articles[index].get('source')
        subject = "News"
        date = articles[index].get('timestamp')
        label = labels[index]

        # Executarea comenzii SQL de inserare
        cur.execute(f"INSERT INTO {selected_dataset} VALUES (?, ?, ?, ?, ?,?)", (title, text, subject, date, label,source))

    # Salvarea modificărilor
    con.commit()
    # Închiderea conexiunii
    con.close()

    return jsonify({"status": "success", "selectedDataSet": selected_dataset})

@app.route('/save-csv', methods=['POST'])
def save_csv_to_database():
    csv_file = request.files['csvFile']
    table_name = request.form.get('table_name')  # Presupunem că table_name este trimis împreună cu cererea
    print(table_name)
    if not table_name:
        return jsonify({"error": "Table name not provided"}), 400

    try:
        # Procesează fișierul CSV și salvează datele în baza de date
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Citește fișierul CSV
        csv_content = csv_file.read().decode('utf-8').split('\n')

        for row in csv_content:
            if row.strip():
                values = row.strip().split(',')
                title = values[0]  # Presupunem că prima coloană este titlul

                # Verifică dacă rândul există deja în tabel
                cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE title = ?", (title,))
                count = cursor.fetchone()[0]

                if count > 0:
                    # Actualizează rândul existent
                    cursor.execute(f"""
                        UPDATE {table_name}
                        SET text = ?, subject = ?, date = ?, label = ?, source = ?
                        WHERE title = ?
                    """, (*values[1:], title))
                else:
                    # Inserează un rând nou
                    cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?)", values)

        conn.commit()
        return jsonify({"success": True}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}


def load_csv_to_db(filepath, table_name, db_path):
    # Conectează-te la baza de date SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Citește primul rând din fișierul CSV pentru a obține numele coloanelor
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # presupune că primul rând este header-ul
        print (headers)
        # Creează tabela, eliminând-o dacă există deja
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        columns = ', '.join([f'"{header}" TEXT' for header in headers])
        cursor.execute(f'CREATE TABLE {table_name} ({columns})')

        # Citește rândurile din CSV și inserează-le în tabelă
        for row in reader:
            placeholders = ', '.join('?' * len(row))
            cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)

    # Salvează modificările și închide conexiunea
    conn.commit()
    conn.close()

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    print (text)
    # Procesarea textului (aici doar ca exemplu inversăm textul)
    processed_text = model_inference.run(text)

    return jsonify({"processedText": processed_text})

if __name__ == '__main__':
    #app.run(debug=True)
    load_csv_to_db('LocalDataSet.csv', 'LocalDataSet', DATABASE_URL)