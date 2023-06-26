import pandas as pd

# Read the CSV file
csv_file = 'input.csv'
df = pd.read_csv(csv_file)

# Convert the DataFrame to XLSX
xlsx_file = 'output.xlsx'
df.to_excel(xlsx_file, index=False)

print("CSV converted to XLSX successfully.")
