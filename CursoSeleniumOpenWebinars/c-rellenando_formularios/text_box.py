'''
caso de teste:(en la pagina wikipedia, y vamos testar en Chrome)
1- entrar en ña pagina wikipedia
2- identificar la caja de texto para busqueda
3- escrever la palabra mar
4- pulsar el boton buscar
5- entrar en la pagina donde se habla del mar

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    # vamos a pruebar com Chrome
    navegador = webdriver.Chrome()   

    # abrimos el navegador pantalla completa                                    
    navegador.maximize_window()

    # vamos a pruebar la pagina wikipedia
    navegador.get("https://wikipedia.es")  

    # quiero que espere 5 segundos
    time.sleep(5)        

    # encuentre el elemento con el id=searchInput( es el textbox para busquedas) y escriba mar
    navegador.find_element(By.ID, "searchInput").send_keys("mar")        

    # quiero que espere 5 segundos
    time.sleep(5) 


    # Buscar el botón de buscar dentro del formulario y hacer clic en él
    boton_de_busqueda = navegador.find_element(By.CSS_SELECTOR, "form#searchform button.cdx-button.cdx-search-input__end-button")
    boton_de_busqueda.click()

    # quiero que espere 5 segundos
    time.sleep(5) 

finally:
    # cerrar todo
    navegador.quit()                                                     


