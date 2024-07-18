import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PyPDF2 import PdfReader
import re
import io

def select_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_label.config(text=f"PDF selecionado: {pdf_path}")
    else:
        pdf_label.config(text="Nenhum PDF selecionado")

def select_excel():
    global excel_path
    excel_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if excel_path:
        excel_label.config(text=f"Excel será salvo em: {excel_path}")
    else:
        excel_label.config(text="Nenhum local selecionado")

def extract_tables_from_pdf(pdf_path):
    tables = []
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()
            lines = page_text.split('\n')
            table = []
            for line in lines:
                if re.match(r'\d{2}/\d{2}/\d{2}', line):  # Check if the line starts with a date
                    table.append(line)
                elif table:  # Append the line to the last row if it's not empty
                    table[-1] += ' ' + line
            tables.extend(table)
    return tables

def generate_excel():
    if pdf_path and excel_path:
        try:
            tables = extract_tables_from_pdf(pdf_path)
            valid_tables_found = False  # Flag to track if at least one valid table is found
            with pd.ExcelWriter(excel_path) as writer:  # Use 'with' to automatically close the writer
                for i, table in enumerate(tables):
                    try:
                        df = pd.read_csv(io.StringIO(table), sep="\s+")
                        # Skip tables with unexpected column counts
                        if len(df.columns) != 10:
                            print(f"Tabela {i+1} possui um número inválido de colunas. Pulando...")
                            continue
                        df.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)
                        valid_tables_found = True  # Set flag to True if a valid table is found
                    except pd.errors.ParserError as e:
                        print(f"Erro ao converter tabela {i+1}: {e}")
            if not valid_tables_found:
                error_message = "Nenhuma tabela válida encontrada no PDF."
                status_label.config(text=error_message)
                print(error_message)
            else:
                status_label.config(text="Conversão concluída com sucesso!")
                print("Conversão concluída com sucesso!")
        except Exception as e:
            error_message = f"Erro ao converter PDF para Excel: {e}"
            status_label.config(text=error_message)
            print(error_message)
    else:
        error_message = "Por favor, selecione um PDF e um local para salvar o arquivo Excel"
        status_label.config(text=error_message)
        print(error_message)


# Criar janela principal
root = tk.Tk()
root.title("Conversor PDF para Excel")

# Criar widgets
pdf_button = tk.Button(root, text="Selecionar PDF", command=select_pdf)
pdf_label = tk.Label(root, text="Nenhum PDF selecionado")

excel_button = tk.Button(root, text="Selecionar Local para Salvar Excel", command=select_excel)
excel_label = tk.Label(root, text="Nenhum local selecionado")

generate_button = tk.Button(root, text="Gerar Excel", command=generate_excel)
status_label = tk.Label(root, text="")

# Organizar widgets na janela
pdf_button.pack(pady=5)
pdf_label.pack()

excel_button.pack(pady=5)
excel_label.pack()

generate_button.pack(pady=10)
status_label.pack()

# Iniciar o loop de eventos
root.mainloop()

