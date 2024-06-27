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
    drive.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_datetime-local")  

    # quiero que espere 5 segundos
    time.sleep(5) 

    # encuentra el Id=accept-choices(es un boton que aparece para Aceptar todo y visitar el sitio web) y pulsar
    elemento = drive.find_element(By.ID,"accept-choices")
    elemento.click()

    # Muda para o frame correto onde está o combobox, muda el sitio
    drive.switch_to.frame("iframeResult")

    #buscamos el elemento por el nombre
    fecha = drive.find_element(By.NAME,"birthdaytime")

    #escribimos la fecha que queremos
    fecha.send_keys("25021983")

    #despues de la fecha tenemos la hora, hay un espacio entre las dos informaciones
    fecha.send_keys(Keys.TAB)

    # quiero que espere 3 segundos
    time.sleep(3) 
    
    #escribimos la hora que queremos
    fecha.send_keys("0830")

    # quiero que espere 3 segundos
    time.sleep(3) 

    # Encontra o botão de submit pelo tipo e clica nele
    submit_button = drive.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()


finally:
    # quiero que espere 5 segundos
    time.sleep(5) 

    # cerrar todo
    drive.quit() 

