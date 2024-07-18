import pyautogui
import pandas as pd 
import time

tabela = pd.read_csv(r"C:\Users\PC\Desktop\Área de Trabalho\ByteVault\PROJETOS\Controllers\DCTF-Automation\DCTF-Automation\tests\dados.csv") # "EMPRESASID.csv = Relatorio Padrão Ajustavel.csv"
print(tabela)

pyautogui.PAUSE = 0.90
for linha in tabela.index:
	pyautogui.doubleClick(510, 62)
	time.sleep(1.5)
	pyautogui.doubleClick(588, 133)
	time.sleep(1.5)
	pyautogui.doubleClick(789, 128)
	time.sleep(1.5)
	pyautogui.doubleClick(x=1019, y=267) #x=1055, y=239)
	time.sleep(1.5)
	pyautogui.doubleClick(x=1306, y=271) #x=1354, y=240)
	time.sleep(1.5)
	data = tabela.loc[linha, "DATA"]
	pyautogui.write(str(tabela.loc[linha, "DATA"]))
	pyautogui.press('enter')
	time.sleep(0.25)
	pyautogui.click(1087, 736) #...
	pyautogui.click(1222, 390) #setinha icon
	pyautogui.click(1181, 425) #clinte M 
	pyautogui.click(x=757, y=468) #pasta DCTF
	pyautogui.click(x=1104, y=678) #Ok 
	pyautogui.click(855, 742) #campo da escrita
	pyautogui.press('left')
	pyautogui.press('left')
	pyautogui.press('left')
	pyautogui.press('left')
	empresa = tabela.loc[linha, "EMPRESA"]
	pyautogui.write(str(tabela.loc[linha, "EMPRESA"]))
	time.sleep(0.20)
	pyautogui.click(1234, 397) #exportar butão
	time.sleep(7)
	pyautogui.click(1026, 605)
	pyautogui.click(1324, 343)
	time.sleep(1)