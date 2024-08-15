import pytesseract
from PIL import Image
import pandas as pd
import requests
#
# Função para extrair texto de uma imagem usando pytesseract
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Função para salvar o texto extraído em um arquivo Excel
def save_text_to_excel(text, excel_path):
    lines = text.splitlines()
    df = pd.DataFrame(lines, columns=["Data"])
    df.to_excel(excel_path, index=False)

# Função para converter imagem em Excel usando a API Imagetoexcel.com
def convert_image_to_excel_with_api(image_path, excel_path, api_key):
    url = 'https://api.imagetoexcel.com/v1/convert'
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        with open(excel_path, 'wb') as f:
            f.write(response.content)
        print(f"Conversão pela API bem-sucedida! O arquivo foi salvo como '{excel_path}'.")
    else:
        print(f"Erro na conversão pela API: {response.status_code}")
        print(response.text)

# Caminho para sua imagem
image_path = r"C:\Users\PC\Downloads\screencapture-tomeconta-tcepe-tc-br-fornecedor-2024-08-12-14_50_49.png"

# Caminho para salvar o arquivo Excel
excel_path = r"C:\Users\PC\Downloads\outresult.xlsx"

# API Key
api_key = 'VoFOlnbugrW4jePEK2lfnBPW9KmKJQ16e5yqcmJk'

# Escolha o método de extração/conversão
use_api = True  # Mude para False se quiser usar o pytesseract

if use_api:
    # Conversão usando a API
    convert_image_to_excel_with_api(image_path, excel_path, api_key)
else:
    # Extração de texto usando pytesseract
    text = extract_text_from_image(image_path)
    # Salvando em Excel
    save_text_to_excel(text, excel_path)
    print(f"Texto extraído foi salvo em {excel_path}")
