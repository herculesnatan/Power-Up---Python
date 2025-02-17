# Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

#pyautogui.hotkey -> atalho de teclado 
pyautogui.PAUSE = 0.7
# abrir o navegador 
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Login no sistema 
pyautogui.click(x=472, y=356)
pyautogui.write("medeiroshercules23@gmail.com")
pyautogui.click(x=391, y=459)
pyautogui.write("senha123")
pyautogui.click(x=702, y=519)


# Passo 3: Importar base de dados
tabela = pandas.read_csv("produtos.csv")

linha = 0

# para cada linha da minha tabela
for linha in tabela.index:  
    # Passo 4: Cadastar um produto
    pyautogui.click(x=593, y=239)
    # Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca do Produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo do Produto 
    tipo_produto = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo_produto))
    pyautogui.press("tab")

    # Categoria do produto 
    categoria_produto = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria_produto))
    pyautogui.press("tab")

    # Preço Unitário do Produto 
    preco_produto = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_produto))
    pyautogui.press("tab")

    # Custo do Produto
    custo = tabela.loc[linha, "custo"] 
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # Clicar no botão enviar
    pyautogui.press("enter")

    # dar scroll de tudo pra cima 
    pyautogui.scroll(5000)
# Passo 5: Repitir o processo de cadastro até acabar os produtos
