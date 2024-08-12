import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageEnhance, ImageOps
import pytesseract
import pandas as pd

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executa o navegador em segundo plano
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')  # Aumenta o tamanho da janela

# Inicialize o WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Pasta contendo os arquivos HTML
folder_path = r'C:\Users\PC\Desktop\2024'  # Substitua pelo caminho da sua pasta

# Lista todos os arquivos HTML na pasta
html_files = [f for f in os.listdir(folder_path) if f.endswith('.htm') or f.endswith('.html')]

def preprocess_image(image):
    # Convert to grayscale
    image = ImageOps.grayscale(image)
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Ajuste o fator conforme necessário
    
    # Binarize the image
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    
    # Optionally, resize the image
    image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
    
    return image

for html_file in html_files:
    html_file_path = os.path.join(folder_path, html_file)
    print(f"Processando: {html_file_path}")

    # Carregue o HTML
    driver.get(f'file://{html_file_path}')

    # Aguarda o carregamento completo da página
    time.sleep(2)  # Ajuste conforme necessário

    # Tira a captura de tela
    screenshot_path = f'{html_file}.png'
    driver.save_screenshot(screenshot_path)

    # Abra a imagem com o PIL
    image = Image.open(screenshot_path)

    # Se você sabe a área específica, use esta área
    # Exemplo: imagem_cortada = image.crop((x1, y1, x2, y2))
    
    # Pré-processamento da imagem
    image = preprocess_image(image)

    # Use o pytesseract para extrair o texto da imagem com opções aprimoradas
    custom_oem_psm_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_oem_psm_config)

    # Divida o texto em linhas e colunas para o Excel
    rows = text.split('\n')
    data = [row.split() for row in rows]

    # Crie um DataFrame do Pandas
    df = pd.DataFrame(data)

    # Salve o DataFrame em uma planilha Excel
    excel_file_path = os.path.join(folder_path, f'{os.path.splitext(html_file)[0]}.xlsx')
    df.to_excel(excel_file_path, index=False)

    # Remova a captura de tela
    os.remove(screenshot_path)

    print(f"Planilha gerada: {excel_file_path}")

driver.quit()
