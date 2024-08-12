import pytesseract
from PIL import Image
import pandas as pd

# Função para extrair texto de uma img
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text  

# Função para salvar texto extraido
def save_text_to_excel(text, excel_path):
    #quebra texto em linhas
    lines = text.splitlines()
    # Cria um dataframe do pandas
    df = pd.DataFrame(lines, columns=["Data"])
    # Salva Dataframe como um arquivo Excel
    df.to_excel(excel_path, index=False)
    
    # Caminho para sua imagem
    image_path = r"C:\Users\PC\Downloads\screencapture-tomeconta-tcepe-tc-br-fornecedor-2024-08-12-14_50_49.png"
    
    # Caminho para salvar o arquivo Excel
    excel_path = r"C:\Users\PC\Downloads\outresult.xlsx"
    
    # Extração de texto
    text = extract_text_from_image(image_path)
    
    # Salvando em Excel
    save_text_to_excel(text, excel_path)
    
    print(f"Texto extraido foi salvo em {excel_path}")
    
