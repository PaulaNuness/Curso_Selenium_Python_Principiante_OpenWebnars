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
