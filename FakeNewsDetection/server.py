import sqlalchemy
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
import pandas as pd
import os
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
DATABASE_URL = 'test.db'


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
        dataSets = [{"text": table[0]} for table in tables]
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

@app.route('/submit_dataset', methods=['POST'])
def submit_dataset():
    data = request.json
    # primestete numele si un link
    selected_dataset = data.get('selectedDataSet')
    website_link = data.get('siteLink')
    label = data.get('selectedValue')
    print(selected_dataset)
    print(website_link)
    print(label)
    # apelez web scraperu cu linku respectiv
    # Definirea valorilor pentru rândul nou
    title = "Test Title"
    text = "This is a test text."
    subject = "Test Subject"
    date = "2024-05-21"  # Formatul datei depinde de cum este definit în baza de date
    label = 1
    con = sqlite3.connect(DATABASE_URL)
    cur = con.cursor()
    # Executarea comenzii SQL de inserare
    cur.execute("""
        INSERT INTO DataSet2 (title, text, subject, Date, label) 
        VALUES (?, ?, ?, ?, ?)
        """, (title, text, subject, date, label))

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
                        SET text = ?, subject = ?, date = ?, label = ?
                        WHERE title = ?
                    """, (*values[1:], title))
                else:
                    # Inserează un rând nou
                    cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)", values)

        conn.commit()
        return jsonify({"success": True}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('/tmp', filename)
        file.save(filepath)

        # Încarcă fișierul CSV în baza de date
        load_csv_to_db(filepath, 'my_table')
        os.remove(filepath)  # Șterge fișierul după ce a fost încărcat

        return jsonify({"status": "success", "message": "File uploaded and data inserted into database"}), 200

    return jsonify({"error": "File type not allowed"}), 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}


def load_csv_to_db(filepath, table_name):
    df = pd.read_csv(filepath)
    df.to_sql(table_name, engine, if_exists='replace', index=False)


if __name__ == '__main__':
    app.run(debug=True)
