import pandas as pd

file_path = '74.xlsx' 
df = pd.read_excel(file_path)

def clean_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))

df['CPF'] = df['CPF'].astype(str).apply(clean_cpf)

cleaned_file_path = '1cleaned_file_path.xlsx' 
df.to_excel(cleaned_file_path, index=False)
