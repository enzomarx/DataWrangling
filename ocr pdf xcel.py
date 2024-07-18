import fitz  # PyMuPDF
import pytesseract
import pandas as pd
from PIL import Image
import io

# Função para extrair texto das imagens usando OCR
def ocr_image(image):
    text = pytesseract.image_to_string(image, lang='por')  # Usar português como exemplo
    return text

# Função para converter PDF em DataFrame
def pdf_to_dataframe(pdf_path):
    # Abrir o PDF
    document = fitz.open(pdf_path)
    rows = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))

        # Realizar OCR na imagem
        text = ocr_image(img)
        # Dividir o texto em linhas
        lines = text.split('\n')

        for line in lines:
            # Assumindo que os dados estão separados por espaços ou tabulações
            # Adapte a lógica conforme a formatação do seu PDF
            if line.strip():
                row = line.split()
                rows.append(row)

    # Criar DataFrame com os dados extraídos
    df = pd.DataFrame(rows)
    return df

# Função para salvar DataFrame em um arquivo Excel
def save_to_excel(df, excel_path):
    df.to_excel(excel_path, index=False)

# Caminho do arquivo PDF e do arquivo Excel de saída
pdf_path = r'C:\Users\Enzo\Documents\CCF11062024.pdf'
excel_path = 'saida.xlsx'

# Converter PDF em DataFrame
df = pdf_to_dataframe(pdf_path)
# Salvar DataFrame em um arquivo Excel
save_to_excel(df, excel_path)
