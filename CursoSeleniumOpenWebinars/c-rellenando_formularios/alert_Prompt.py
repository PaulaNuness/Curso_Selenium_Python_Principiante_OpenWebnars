from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    # Inicializa o driver do Firefox
    driver = webdriver.Firefox()

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Navega para a página de exemplo do W3Schools para o prompt
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")

    # Aguarda o carregamento da página
    time.sleep(3)

    # Aceita cookies se o botão aparecer
    try:
        accept_button = driver.find_element(By.ID, "accept-choices")
        accept_button.click()
    except:
        pass  # Se o botão de aceitação de cookies não estiver presente, continua sem problemas.

    # Muda para o iframe que contém o botão "Try it"
    driver.switch_to.frame(0)  # Neste caso, o prompt está no primeiro (e único) iframe

    # Encontra o botão "Try it" e clica nele
    try_button = driver.find_element(By.XPATH, '//button[text()="Try it"]')
    try_button.click()

    # Aguarda o prompt aparecer (esperamos que o usuário o preencha manualmente)
    time.sleep(2)

    # Switch para o prompt
    prompt = driver.switch_to.alert

    # Limpa o texto atual do prompt
    prompt.send_keys(Keys.CONTROL + "a")  # Seleciona todo o texto no prompt
    prompt.send_keys(Keys.DELETE)  # Deleta o texto selecionado

    # Aguarda 2 segundos
    time.sleep(2)

    # Envia um novo texto para o prompt
    prompt.send_keys("Paula Nunes")

    # Aguarda 2 segundos
    time.sleep(2)

    # Aceita o prompt
    prompt.accept()

    # Aguarda 2 segundos
    time.sleep(2)

    # Clica novamente no botão "Try it"
    try_button.click()

    # Aguarda o prompt aparecer novamente
    time.sleep(2)

    # Switch para o prompt
    prompt = driver.switch_to.alert

    # Cancela o prompt
    prompt.dismiss()

    # Aguarda 2 segundos
    time.sleep(2)

finally:
    # Aguarda alguns segundos antes de fechar o navegador
    time.sleep(5)

    # Fecha o navegador
    driver.quit()
