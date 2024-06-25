from selenium import webdriver
############################################################################################################################################
# import By: utilizada para localizar elementos no DOM de uma página web.
from selenium.webdriver.common.by import By
""" 
ID:----------------Localiza um elemento pelo seu atributo id.--------------element = driver.find_element(By.ID, "element_id")
NAME:--------------Localiza um elemento pelo seu atributo name.------------element = driver.find_element(By.NAME, "element_name")
XPATH:-------------Localiza um elemento usando uma expressão XPath.--------element = driver.find_element(By.XPATH, "//tagname[@attribute='value']")
LINK_TEXT:---------Localiza um link (elemento <a>) pelo texto completo do link.-------element = driver.find_element(By.LINK_TEXT, "link text")
PARTIAL_LINK_TEXT:-Localiza um link (elemento <a>) por uma parte do texto do link.----element = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
TAG_NAME:----------Localiza elementos pelo nome da tag HTML.---------------element = driver.find_element(By.TAG_NAME, "tagname")
CLASS_NAME:--------Localiza elementos pelo atributo class.-----------------element = driver.find_element(By.CLASS_NAME, "classname")
CSS_SELECTOR:------Localiza elementos usando um seletor CSS.---------------element = driver.find_element(By.CSS_SELECTOR, "css_selector")

"""
############################################################################################################################################
# import Keys: é uma ferramenta poderosa para simular a entrada de teclado e enviar teclas especiais para elementos web.
from selenium.webdriver.common.keys import Keys
'''
Keys.RETURN ou Keys.ENTER:   Tecla Enter
Keys.TAB:                    Tecla Tab
Keys.ESCAPE:                 Tecla Escape
Keys.BACKSPACE:              Tecla Backspace
Keys.DELETE:                 Tecla Delete
Keys.CONTROL (ou Keys.CTRL): Tecla Control (Ctrl)
Keys.SHIFT:                  Tecla Shift
Keys.ALT:                    Tecla Alt
Keys.SPACE:                  Tecla Espaço
Keys.ARROW_UP:               Seta para cima
Keys.ARROW_DOWN:             Seta para baixo
Keys.ARROW_LEFT:             Seta para a esquerda
Keys.ARROW_RIGHT:            Seta para a direita
Keys.HOME:                   Tecla Home
Keys.END:                    Tecla End
Keys.PAGE_UP:                Tecla Page Up
Keys.PAGE_DOWN:              Tecla Page Down
'''
############################################################################################################################################
# mecanismo de espera
import time
############################################################################################################################################

try:
    # Inicializar el navegador sin especificar la ruta del chromedriver, porque ya tenemos la ruta en variables de entorno
    driver = webdriver.Chrome()

    # Buscar(navegar) en  la pagina de wikipedia
    driver.get("https://www.wikipedia.es")

    # Escribimos en el terminal el titulo de la pagina web
    print(driver.title)

    # Busca  link que tenha el id
    element = driver.find_element(By.ID, "vector-main-menu-dropdown")

    # Espera 2 segundos antes de fechar o navegador
    time.sleep(2)

    # clicar no elemento
    element.click()
    print("Elemento 1 hamburguer clicado com sucesso")

    # Espera 2 segundos 
    time.sleep(2)

    # Encontra o link "Página aleatoria" 
    pagina_aleatoria = driver.find_element(By.XPATH, '//a[@href="/wiki/Especial:Aleatoria"]')
    print("Elemento encontrado:", pagina_aleatoria)

    # Clicar en el enlace pagina_aleatoria
    pagina_aleatoria.click()
    print("Elemento 2 enlace página aleatoria clicado com sucesso")


except Exception as e:
    print("Elemento não encontrado")
    print("Erro:", e)
    
finally:

    # Espera 10 segundos antes de fechar o navegador
    time.sleep(5)
    #cierra el navegador y la session del driver
    driver.quit()

############################################################################################################################################