import pyautogui

def automatizar_cliques(n_cliques):
    for i in range(n_cliques):
        # Localizar e executar
        pyautogui.click(localizacao_botao)
        # ...

# quantidade de repetições
n_cliques = 100

# Chamar
automatizar_cliques(n_cliques)

#######################################
import pyautogui

def extrair_dados_csv(arquivo_csv):
    with open(arquivo_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for linha in reader:
            # Extrair dados da linha atual 
            nome = linha[0]
            email = linha[1]
            # Usar pyautogui para preencher 
            pyautogui.click(localizacao_campo_nome)
            pyautogui.write(nome)
            pyautogui.click(localizacao_campo_email)
            pyautogui.write(email)
            # ...

# Chamar 
extrair_dados_csv('dados.csv')
