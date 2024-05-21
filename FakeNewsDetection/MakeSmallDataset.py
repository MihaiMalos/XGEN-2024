import pandas as pd

# Load the CSV file
file_path = 'FakeReal.csv'
df = pd.read_csv(file_path)

# Get the first 20 rows
df_first_20_rows = df.head(20)

# Save the first 20 rows to a new CSV file
output_path = 'FakeRealSmall.csv'
df_first_20_rows.to_csv(output_path, index=False)
