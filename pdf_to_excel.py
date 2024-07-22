import tabula
import fitz  
import pytesseract
from pdf2image import convert_from_path
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_tables_with_tabula(pdf_path):
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
        return tables
    except Exception as e:
        print(f"Error using tabula for {pdf_path}: {e}")
        return None

def extract_text_with_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"
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

def save_tables_to_excel(tables, writer, sheet_name):
    if tables:
        combined_df = pd.concat([pd.DataFrame(table) for table in tables], ignore_index=True)
        combined_df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

def convert_pdf_to_excel(pdf_path, writer, sheet_name):
    tables = extract_tables_with_tabula(pdf_path)
    
    if not tables:
        text = extract_text_with_ocr(pdf_path)
        tables = extract_tables_from_text(text)
    
    save_tables_to_excel(tables, writer, sheet_name)

pdf_paths = ["12-DEZEMBRO (2).pdf", "Balanco socio ostensivo 2022 (2) (2).pdf"]
excel_path = "combined_output4.xlsx"

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for i, pdf_path in enumerate(pdf_paths):
        sheet_name = f'Arquivo_{i+1}'
        convert_pdf_to_excel(pdf_path, writer, sheet_name)
