import time
import pyautogui
import pandas as pd


tabela = pd.read_csv(r'C:\Users\PC\Desktop\infor.csv')
pyautogui.PAUSE = 0.4

pyautogui.hotkey('alt', 'a')
pyautogui.hotkey('shift', 's')
pyautogui.click(x=438, y=170) #Volta para a primeira
pyautogui.click(x=356, y=246) #clica na data
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(x=451, y=280)

def inclui_sc(linha):
    time.sleep(0.4)    
    pyautogui.click(265, 306)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.write(str('150'))
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'n') #aperta em incluir
    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press('tab')
    pyautogui.write('83,67') #preenche participação
    pyautogui.press('tab')
    pyautogui.write('150') #quotas integralizadas
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1') #valor da quota
    pyautogui.press('tab')
    pyautogui.write('150') #capital integralizado
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'n')

def inclui_ost():
    pyautogui.sleep(0.4)
    pyautogui.write(str(21609217000173))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('29,28') #quotas integralizadas
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1') #valor da quota
    pyautogui.press('tab')
    pyautogui.write('29,28') #capital integralizado
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.press('tab')     


    
for linha in range(len(tabela)):
    inclui_sc(linha)
    inclui_ost()