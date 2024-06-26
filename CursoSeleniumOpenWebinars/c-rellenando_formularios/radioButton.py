from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # vamos a pruebar com Chrome    
    drive = webdriver.Chrome()

    # abrimos el navegador pantalla completa                                    
    drive.maximize_window()

    # vamos a pruebar la pagina donde hay combobox
    drive.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")  

    # quiero que espere 5 segundos
    time.sleep(5) 

    # encuentra el Id=accept-choices(es un boton que aparece para Aceptar todo y visitar el sitio web) y pulsar
    elemento = drive.find_element(By.ID,"accept-choices")
    elemento.click()

    time.sleep(3)
    
    # Muda para o frame correto onde está o combobox
    drive.switch_to.frame("iframeResult")

    # Seleciona os radio buttons pelos IDs e clica neles
    fav_language_html = drive.find_element(By.ID, "html")
    fav_language_html.click()

    age_31_60 = drive.find_element(By.ID, "age2")
    age_31_60.click()

    # Encontra o botão de submit pelo valor do atributo 'value' e clica nele
    submit_button = drive.find_element(By.XPATH, '//input[@value="Submit"]')
    submit_button.click()

    # Espera 5 segundos para visualizar a ação
    time.sleep(5)


finally:
    # quiero que espere 5 segundos
    time.sleep(5) 

    # cerrar todo
    drive.quit() 

