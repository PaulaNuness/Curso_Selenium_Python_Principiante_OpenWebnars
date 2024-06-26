from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

navegador = webdriver.Chrome()

navegador.implicitly_wait(10)

navegador.get("http:coniemenezes.com")
print(navegador.title)
time.sleep(5)
navegador.save_screenshot('print1.png')
elemento_contato = navegador.find_element(By.LINK_TEXT,"Contato")
time.sleep(5)
elemento_contato.click()
time.sleep(5)
navegador.save_screenshot('print2.png')
time.sleep(5)
navegador.quit()