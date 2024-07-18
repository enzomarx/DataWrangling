import fitz  # PyMuPDF
import pytesseract
import pandas as pd
from PIL import Image
import io

def ocr_image(image):
    text = pytesseract.image_to_string(image, lang='por')  # Usar português como exemplo
    return text

def pdf_to_dataframe(pdf_path):
    document = fitz.open(pdf_path)
    rows = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))

        text = ocr_image(img)
        lines = text.split('\n')

        for line in lines:
            # Condição: Assumindo que os dados estão separados por tabulações
            if line.strip():
                row = line.split()
                rows.append(row)

    # Criar DataFrame 
    df = pd.DataFrame(rows)
    return df

def save_to_excel(df, excel_path):
    df.to_excel(excel_path, index=False)

# Caminhos
pdf_path = r'C:\Users\Enzo\Documents\CCF11062024.pdf'
excel_path = 'saida.xlsx'

df = pdf_to_dataframe(pdf_path)

save_to_excel(df, excel_path)
