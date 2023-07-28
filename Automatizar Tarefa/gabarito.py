# Primeiro tem instalar extensao python no computador
# Segundo passo e istalar a extensao pyton no vs code
# Terceiro istalar blibioteca no vs code
# Tem que abrir terminal e no terminal abrir  pront comand 
# No pront comand digita pip install pyautogui
# Assim istala a blibioteca

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
#Dua teclas de atalho  ou mais
# pyautogui.hotkey("ctrl","c" ,"a")

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
# Instalar a blibioteca pandas 
# pront de comando codigo: pip install pandas 
# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd
# as e apelido entao agora pandas sera pd pode fazer outros tb
tabela = pd.read_csv("produtos.csv")
# cria uma variavel tabela =panda ou pd que vai ler arquivo csv
#pode ler qualauqer arquivo so escolher read_ e escolhe o arquivo
print(tabela)
#vai printar o arquivo em tabela
# Passo 4: Cadastrar um produto
#a linha começa em 0 no arquivo tabela começando pelo index da tabela
#ate o final do index
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    #sobe a tabela da tela o scroll barrinha do lado esse numero tem ficar
    # testando no pegar posição ate da certo
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
