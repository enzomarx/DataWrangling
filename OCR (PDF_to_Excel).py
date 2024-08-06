import fitz 
import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

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
    else:
        pd.DataFrame().to_excel(writer, sheet_name=sheet_name)

def convert_pdf_to_excel(pdf_path, writer, sheet_name):
    try:
        text = extract_text_with_ocr(pdf_path)
        tables = extract_tables_from_text(text)
        save_tables_to_excel(tables, writer, sheet_name)
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        pd.DataFrame().to_excel(writer, sheet_name=sheet_name)

def process_folder():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    pdf_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
    if not pdf_paths:
        messagebox.showerror("Erro", "Nenhum arquivo PDF encontrado na pasta selecionada.")
        return
    
    excel_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not excel_path:
        return
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for i, pdf_path in enumerate(pdf_paths):
            sheet_name = f'Arquivo_{i+1}'
            convert_pdf_to_excel(pdf_path, writer, sheet_name)
    
    messagebox.showinfo("Sucesso", f"Arquivos PDF convertidos e salvos em {excel_path}")

# Interface Tkinter
root = tk.Tk()
root.title("Conversor de PDF para Excel")

btn_select_folder = tk.Button(root, text="Selecionar Pasta", command=process_folder)
btn_select_folder.pack(pady=20)

root.mainloop()
