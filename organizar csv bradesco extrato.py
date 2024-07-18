import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Bradesco_04092023_172551.csv")

# Drop rows with any NaN values
df.dropna(inplace=True)

# Reset the index after dropping rows
df.reset_index(drop=True, inplace=True)

# Find the index of the row where the column starts with "Data"
indice_data = df[df['nome_da_coluna'].str.startswith("Data")].index[0]

# Skip rows until the row with the column names
df = pd.read_csv("caminho_para_seu_arquivo.csv", skiprows=indice_data)

# Reset the column names
df.columns = df.iloc[0]
df = df.iloc[1:]

# Reset the index after resetting the column names
df.reset_index(drop=True, inplace=True)

# Save the DataFrame to a new CSV file
df.to_csv("novo_arquivo.csv", index=False)

