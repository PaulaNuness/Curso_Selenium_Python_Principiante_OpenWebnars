
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    # vamos a pruebar com Chrome    
    drive = webdriver.Chrome()

    # abrimos el navegador pantalla completa                                    
    drive.maximize_window()

    # vamos a pruebar la pagina donde hay combobox
    drive.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")  

    # quiero que espere 3 segundos
    time.sleep(3) 

    # encuentra el Id=accept-choices(es un boton que aparece para Aceptar todo y visitar el sitio web) y pulsar
    elemento = drive.find_element(By.ID,"accept-choices")
    elemento.click()

    # Muda para o frame correto onde está o botao Try it, muda el sitio
    drive.switch_to.frame("iframeResult")

    # quiero que espere 2 segundos
    time.sleep(2) 

    # Encontrar el botón por su texto y hacer clic en él
    boton = drive.find_element(By.XPATH, '//button[text()="Try it"]')
    boton.click()

    # quiero que espere 3 segundos
    time.sleep(3) 

    # Muda para o alert onde está o botao aceptar, 
    drive.switch_to.alert.accept()

finally:
    # quiero que espere 3 segundos
    time.sleep(3) 

    # cerrar todo
    drive.quit() 

