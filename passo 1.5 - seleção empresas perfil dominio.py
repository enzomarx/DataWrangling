import pyautogui
import pandas as pd
import time

tabela = pd.read_csv(r"C:\Users\PC\Desktop\Área de Trabalho\ByteVault\PROJETOS\Controllers\DCTF-Automation\DCTF-Automation\tests\dados.csv") # "EMPRESASID.csv = Relatorio Padrão Ajustavel.csv"
print(tabela)

pyautogui.PAUSE = 0.3
for linha in tabela.index:
	pyautogui.click(162, 113)
	time.sleep(0.25)
	data = tabela.loc[linha, "CODIGO"]
	pyautogui.write(str(tabela.loc[linha, "CODIGO"]))
	pyautogui.press('enter')
	time.sleep(3)

#esse passo precisa ser acoplado no passo 2.
