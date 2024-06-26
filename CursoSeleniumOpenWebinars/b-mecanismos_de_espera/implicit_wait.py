from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.implicitly_wait(15)

navegador.get("http:coniemenezes.com")
print(navegador.title)
navegador.implicitly_wait(15)
navegador.save_screenshot('print1.png')
elemento_contato = navegador.find_element(By.LINK_TEXT,"Contato")
navegador.implicitly_wait(15)
elemento_contato.click()
navegador.save_screenshot('print2.png')
navegador.implicitly_wait(15)
navegador.quit()