import pyautogui
import time


# LEMBRE-SE, SE TRATA DE UM 'BOTÃO' E NÃO UM COMANDO EM SI.

# COMANDOS PARA ENTRAR NO SISTEMA E NAVEGADOR

pyautogui.PAUSE = 0.5

pyautogui.press('win') # -> COMANDO PARA PRESSIONAR O BOTÃO WINDOWNS DO TECLADO
pyautogui.write('edge') # -> COMANDO PARA DIGITAR TEXTO DO TECLADO'
pyautogui.press('enter') # -> COMANDO PARA PRESSIONAR A TECLA 'ENTER' DO TECLADO

# ENTRAR NO NAVEGADOR

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# ESPERAR O SITE CARREGAR, DANDO UMA PAUSA USANDO O SLEEP
time.sleep(3)
pyautogui.click(x=701, y=447)
pyautogui.write('davi.cms@gmail.com')
pyautogui.press('tab')
pyautogui.write('cms1235')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# PREENCHER OS DADOS DE ACORDO COM O BANCO DE DADOS

import pandas as pd

tabela = pd.read_csv('produtos.csv')

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=631, y=300)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)


