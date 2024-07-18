import pdfplumber

def extract_table_to_csv(pdf_path, output_csv_path):
    """Extracts table data from a PDF and saves it as a CSV file."""
    with pdfplumber.open(pdf_path) as pdf:
        # estou considerando que a tabela esta na primeira pagina
        page = pdf.pages[0]
        
        tables = page.extract_tables()

        if tables:
            # extraindo tabela da 1meira pagina
            table_data = tables[0] 

            # convertendo a tabela em um csv
            csv_data = "\n".join([",".join(map(str, row)) for row in table_data])

            # guardar
            with open(output_csv_path, "w", encoding="utf-8") as f:
                f.write(csv_data)
            print(f"Table data extracted to: {output_csv_path}")
        else:
            print("No tables found on the page.")

# Substitua pelo caminho real do arquivo PDF e pelo caminho do arquivo CSV de saída desejado
pdf_file_path = "arq.PDF"
output_csv_path = "extracted_table_data.csv"

extract_table_to_csv(pdf_file_path, output_csv_path)