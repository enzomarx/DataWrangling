import pandas as pd
import re

# Load CSV 
file_path = r'C:\Users\PC\Desktop\ago.csv'
cnpj_data = pd.read_csv(file_path, header=None)

# formatar CNPJ
def format_cnpj(cnpj):
    formatted = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', str(cnpj))
    return formatted

cnpj_data[0] = cnpj_data[0].apply(format_cnpj)

# salvar cnpj limpos em um novo csv
formatted_file_path = r'C:\Users\PC\Desktop\formatted_cnpjs.csv'
cnpj_data.to_csv(formatted_file_path, index=False, header=False)

print(f"Formatted CNPJs have been saved to {formatted_file_path}")
