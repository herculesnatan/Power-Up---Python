# Case: Abrir o sistema de cadastramento de produtos, logar, cadastrar os produtos

import pyautogui
import pandas

pyautogui.PAUSE = 0.5
link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o Edge e entrar no sistema
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.write(link_sistema)
pyautogui.press("enter")

# digitar email e senha 
email = "email@email.com"
senha = "senha123"
pyautogui.click(x=508, y=353)
pyautogui.write(email)
pyautogui.click(x=392, y=452)
pyautogui.write(senha)
pyautogui.click(x=676, y=519) # para entrar no sistema

# importar a tabela de produtos
tabela_produto = pandas.read_csv("produtos.csv")

# iniciar os produtos na linha 0 
linha = 0

# pegar posição dos campos para preencher com os produtos
for linha in tabela_produto.index:    
    # código produto 
    pyautogui.click(x=395, y=244)
    codigo_produto = tabela_produto.loc[linha, "codigo"]
    pyautogui.write(str(codigo_produto))
    pyautogui.press("tab")

    # marca produto
    marca_produto = tabela_produto.loc[linha, "marca"]
    pyautogui.write(str(marca_produto))
    pyautogui.press("tab")

    # tipo produto 
    tipo_produto = tabela_produto.loc[linha, "tipo"]
    pyautogui.write(str(tipo_produto))
    pyautogui.press("tab")

    # categoria produto 
    categoria_produto = tabela_produto.loc[linha, "categoria"]
    pyautogui.write(str(categoria_produto))
    pyautogui.press("tab")

    # preço unitário do produto 
    preco_produto = tabela_produto.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_produto))
    pyautogui.press("tab")

    # custo do produto 
    custo_produto = tabela_produto.loc[linha, "custo"]
    pyautogui.write(str(custo_produto))
    pyautogui.press("tab")


    # Nem todos produtos tem OBS, então vamos usar uma condição
    obs_produto = tabela_produto.loc[linha, "obs"]
    if not pandas.isna(obs_produto): 
        # OBS
        pyautogui.write(str(obs_produto))
    pyautogui.press("tab")

    # clicar no botão de enviar
    pyautogui.press("enter")

    # dar um scroll para cima 
    pyautogui.scroll(5000)