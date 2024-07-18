import pandas as pd

# CSV -> DataFrame
df = pd.read_csv("Bradesco_04092023_172551.csv")

# Eliminar linhas com quaisquer valores NaN
df.dropna(inplace=True)

# Reset the index 
df.reset_index(drop=True, inplace=True)

# Find index -cabeça "Data"
indice_data = df[df['nome_da_coluna'].str.startswith("Data")].index[0]

df = pd.read_csv("caminho_para_seu_arquivo.csv", skiprows=indice_data)

# Reset the column 
df.columns = df.iloc[0]
df = df.iloc[1:]

# Reset the index 
df.reset_index(drop=True, inplace=True)

df.to_csv("novo_arquivo.csv", index=False)

