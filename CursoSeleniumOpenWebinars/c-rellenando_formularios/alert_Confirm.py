from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Navega para a página de exemplo do W3Schools para a caixa de confirmação
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")

    # Aguarda o carregamento da página
    time.sleep(3)

    # Aceita cookies se o botão aparecer
    try:
        accept_button = driver.find_element(By.ID, "accept-choices")
        accept_button.click()
    except:
        pass  # Se o botão de aceitação de cookies não estiver presente, continua sem problemas.

    # Muda para o iframe que contém o botão "Try it"
    driver.switch_to.frame("iframeResult")

    # Aguarda o carregamento do iframe
    time.sleep(2)

    # Encontra o botão "Try it" e clica nele
    try_button = driver.find_element(By.XPATH, '//button[text()="Try it"]')
    try_button.click()

    # Aguarda 2 segundos
    time.sleep(2)

    # Muda para o alerta e aceita-o
    alert = driver.switch_to.alert
    alert.accept()


    # Aguarda 3 segundos
    time.sleep(3)

    # Encontra o botão "Try it" e clica nele novamente
    try_button.click()

    # Aguarda 3 segundos
    time.sleep(3)

    # Muda para o alerta e descarta-o
    alert = driver.switch_to.alert
    alert.dismiss()


finally:
    # Aguarda alguns segundos antes de fechar o navegador
    time.sleep(5)

    # Fecha o navegador
    driver.quit()
