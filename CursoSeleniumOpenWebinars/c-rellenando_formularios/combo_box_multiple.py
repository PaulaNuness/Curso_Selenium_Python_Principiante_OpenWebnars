from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  #es ara trabajar com combobox
import time

try:
    # vamos a pruebar com Chrome    
    drive = webdriver.Chrome()

    # abrimos el navegador pantalla completa                                    
    drive.maximize_window()

    # vamos a pruebar la pagina donde hay combobox
    drive.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")  

    # quiero que espere 5 segundos
    time.sleep(5) 

    # encuentra el Id=accept-choices(es un boton que aparece para Aceptar todo y visitar el sitio web) y pulsar
    elemento = drive.find_element(By.ID,"accept-choices")
    elemento.click()

    # Muda para o frame correto onde está o combobox
    drive.switch_to.frame("iframeResult")

    # Seleciona o combobox pelo ID
    select_element = Select(drive.find_element(By.ID, "cars"))

    # Seleciona a opção "Audi"
    select_element.select_by_value("audi")
    select_element.select_by_value("opel")

    #Encuentra el elemento que es un input e que tenha o valor = Submit y clica nele
    drive.find_element(By.XPATH, '//input[@value="Submit"]').click()



finally:
    # quiero que espere 5 segundos
    time.sleep(5) 

    # cerrar todo
    drive.quit() 