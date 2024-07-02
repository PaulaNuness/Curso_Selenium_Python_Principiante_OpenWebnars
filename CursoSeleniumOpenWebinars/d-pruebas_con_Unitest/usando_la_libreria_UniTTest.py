import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time

class PruebaPython(unittest.TestCase):

    def setUp(self):
        print("\033[94mEjecuto antes de cada test\033[0m")  # Azul
        try:
            # Inicializa o driver do Chrome
            self.driver = webdriver.Chrome()

            # Maximiza a janela do navegador
            self.driver.maximize_window()

            time.sleep(3)
            
        except WebDriverException as e:
            self.fail(f"\033[91mNo se pudo iniciar el navegador: {e}\033[0m")  # Rojo

########################################################################################################################

    def test_uno(self):
        print("\033[92mSoy el test 1\033[0m")  # Verde
        
        try:
            
            # vamos a Google esperamos y pulsamos o botao aceptar
            self.driver.get("https://www.google.com")

            time.sleep(3)

            accept_button = self.driver.find_element(By.ID, "L2AGLb")
            accept_button.click()
    
            time.sleep(3)

            # buscamos o campo de busqueda y escrevemos wikipedia
            busqueda = self.driver.find_element(By.NAME,"q")
            busqueda.send_keys("wikipedia")
            time.sleep(2)
            busqueda.send_keys(Keys.ENTER)

            # vou encontrar o enlace y pulsar 
            pagina_wikipedia = self.driver.find_element(By.XPATH, '//a[@href="https://es.wikipedia.org/wiki/Wikipedia:Portada"]')
            pagina_wikipedia.click()

            # ahora vamos comprobar que eu titulo de la pagina es Wikipedia, la enciclopedia libre.
            titulo = self.driver.title
            self.assertEqual("Wikipedia, las enciclopedia libre",titulo) # si pongo asi va fallar

            print("\033[92mTest 1 concluido con suceso!!!\033[0m")  # Verde
        except Exception as e:
            self.fail(f"\033[91mEl test 1 falló: {e}\033[0m")  # Rojo

########################################################################################################################

    def tearDown(self):
        print("\033[94mEjecuto despues de cada test\033[0m")  # Azul
        time.sleep(3)
        self.driver.quit()

########################################################################################################################

if __name__ == "__main__":
    unittest.main(exit=False)
