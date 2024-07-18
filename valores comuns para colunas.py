import pandas as pd
import re

# Load the CSV file
file_path = r'C:\Users\PC\Desktop\ago.csv'
cnpj_data = pd.read_csv(file_path, header=None)

# Function to format CNPJ
def format_cnpj(cnpj):
    formatted = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', str(cnpj))
    return formatted

# Apply the formatting function to all CNPJs in the dataframe
cnpj_data[0] = cnpj_data[0].apply(format_cnpj)

# Save the formatted CNPJs back to a new CSV file
formatted_file_path = r'C:\Users\PC\Desktop\formatted_cnpjs.csv'
cnpj_data.to_csv(formatted_file_path, index=False, header=False)

print(f"Formatted CNPJs have been saved to {formatted_file_path}")
