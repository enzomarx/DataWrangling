import pandas as pd

#carregar excel file
file_path = 'xxxxxx//xxxxx//xxxxx'
excel_data = pd.ExcelFile(file_path)

# listar todas as planilhas de um arq excel
sheet_names = excel_data.sheet_names[:280] 

# Função para extrair a linha 6 e o conteudo da seção "Sécios e Administradores"
def extract_data(df):
    #extrair a linha 6
    line_6 = df.iloc[5:6]

    # Encontrar o indice da linha onde começa a seção "Sécios e Administradores"
    start_index = df[df.iloc[:, 0].astype(str).str.contains("Sécios e Administradores", na=False)].index
    if not start_index.empty:
        # entao extrair tudo da seção
        section_data = df.iloc[start_index[0]+1:]
    else:
        section_data = pd.DataFrame() # se a seção nao for enconrada, retornar dataframe
    
    return line_6, section_data

# dicionario para armazenar resultados
extract_data = {}

# Extrair dados das planilhas "Arquivo_1" a "Arquivo_280"
updated_sheets = {}
for sheet in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet)
    line_6, section_data = extract_data[sheet]
    updated_sheets[sheet] = add_data(df, line_6, section_data)

# Salvar todas as planilhas atualizadas em um novo arquivo excel
output_path = 'xxxx/xxxxx/xxxxx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet_name, df in updated_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

output_path

