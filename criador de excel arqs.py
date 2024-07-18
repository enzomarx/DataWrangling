#cria planilha do excel
import openpyxl

# Cria um novo arquivo Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Pede ao usuário para inserir os textos separados por vírgula
textos = input("Digite os textos separados por vírgula: ").split(',')

# Escreve os textos na primeira coluna do arquivo Excel
for i, texto in enumerate(textos, start=1):
    sheet.cell(row=i, column=1).value = texto

# Salva o arquivo Excel
nome_arquivo = input("Digite o nome do arquivo Excel: ")
workbook.save(f"{nome_arquivo}.xlsx")

print(f"Os textos foram escritos no arquivo Excel '{nome_arquivo}.xlsx' com sucesso.")