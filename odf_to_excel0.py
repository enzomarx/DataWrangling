import fitz  # PyMuPDF
import pandas as pd

def extract_text_from_first_page(pdf_path):
    document = fitz.open(pdf_path)
    first_page = document.load_page(0)
    text = first_page.get_text("text")
    return text

def extract_tables_from_text(text):
    lines = text.split('\n')
    tables = []
    table = []
    for line in lines:
        if line.strip() == "":
            if table:
                tables.append(table)
                table = []
        else:
            table.append(line.split())
    if table:
        tables.append(table)
    return tables

def save_tables_to_excel(tables, excel_path):
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for i, table in enumerate(tables):
            df = pd.DataFrame(table)
            df.to_excel(writer, sheet_name=f'Tabela_{i+1}', index=False, header=False)

pdf_paths = ["12-DEZEMBRO (2).pdf", "Balanco socio ostensivo 2022 (2) (2).pdf"]
excel_paths = ["12-DEZEMBRO.xlsx", "Balanco_socio_ostensivo_2022.xlsx"]

for pdf_path, excel_path in zip(pdf_paths, excel_paths):
    text = extract_text_from_first_page(pdf_path)
    tables = extract_tables_from_text(text)
    save_tables_to_excel(tables, excel_path)
