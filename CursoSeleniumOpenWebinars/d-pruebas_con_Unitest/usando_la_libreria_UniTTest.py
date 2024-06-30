import unittest
from selenium import webdriver

# tenemos que ayslar cada una de las pruebas
# creamos una clase que hereda de unittes
# defsetUp --> ira ejecutarse al inicio de una prueba
# deftearDown --> ira ejecutarse al final de una prueba
# ejemplo:
#   Ejecutar setUp()
#   Ejecutar test_uno()
#   Ejecutar tearDown()
#   Ejecutar setUp()
#   Ejecutar test_dos()
#   Ejecutar tearDown()


class PruebaPython(unittest.TestCase):

    def setUp(self):
        #pasos previos a cada test

    def tearDown(self):
        #pasos posteriores a cada test

    def test_uno(self):
        #test uno
        #aserción uno

    def test_dos(self):
        #test dos
        #aserción dos


if __name__ == "__main__":
    unittest.main()