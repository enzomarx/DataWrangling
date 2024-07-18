import camelot
import pandas as pd

# Função para extrair tabelas de um PDF e convertê-las em DataFrame
def pdf_to_dataframe(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all')
    dataframes = [table.df for table in tables]
    return dataframes

# Função para salvar DataFrames em um arquivo Excel
def save_to_excel(dataframes, excel_path):
    with pd.ExcelWriter(excel_path) as writer:
        for i, df in enumerate(dataframes):
            df.to_excel(writer, sheet_name=f'Tabela_{i+1}', index=False)

# Caminho do arquivo PDF e do arquivo Excel de saída
pdf_path = r'C:\Users\Enzo\Documents\CCF11062024.pdf'
excel_path = 'saida.xlsx'

# Extrair tabelas do PDF e convertê-las em DataFrames
dataframes = pdf_to_dataframe(pdf_path)
# Salvar DataFrames em um arquivo Excel
save_to_excel(dataframes, excel_path)
