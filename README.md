# Curso_Selenium_Python_Principiante_OpenWebnars
* Curso hecho en la plataforma OpenWebnars
## Introducción
* Selenium es un framework destinado a la automatización de navegación web.
* Podemos encontrar tres versiones disponibles:
  * Selenium IDE --> podemos grabar lo pasos de las pruebas, es 
  sencillo utilizar.
  * Selenium Webdriver --> es uba libreria, disponible en varios leguajes de programacion, requiere un drive(controlador), ChromeDriver(Chrome) o Geckodriver(Firefox)
  * Selenium Grid --> es un servidor de Selenium, es parecido con Jenkins
* Automatizacion de toda tarea repetitiva, utilizando Selenium, para disminuir costes, para ejecutar todas las pruebas necesarias, para hacer las pruebas de regression...
* Pasos en el Selenium IDE:
  * Instalar Firefox o tambien podemos utilizar Chrome y descargar una extension Selenium IDE
  * Abrir el navegador Firefox --> pulsar en los tres puntos --> pulsar complementos --> escribir selenium --> pulsar enter --> selecionar selenium Ide --> ADD
  * Abrimos una nueva ventana en el navegador Firefox --> Pulsamos en la extension Selenium --> abrirá una nueva ventana de selenium
  * Creamos un nuevo proyecto
  * Escribo la URL que vamos trabajar,por ejemplo: https://www.google.com
  * Abrirá una nueva ventana de google, que será la URL de vamos trabajar
  * Pulsamos dentro de la ventana Google los pasos que queremos ejecutar
  * Pulsamos el boton stop, para parar la gravacion
  * Damos un nombre al teste
  * Ya podemos cerrar la ventana google
  * Todos los pasos que hay en el IDE son editables
  * Ahora podemos dar play
  * Hay varios comandos, es todo editable.
**************************************************************************************************************************************
## Descargar Selenium
* Voy hacer en Visual Studio Code:
  * Crear una carpeta donde quieras
  * Dentro del Visual Studio Code, entrar en la carpeta
  * Abrir un terminal, escribir: pip install selenium
  * Se deseo ver la version escribo: pip list
* Ahora descargar driver para Chrome
  * Devemos saber la version de Chrime que tenemos
  * Vamos a :  https://chromedriver.chromium.org/ --> bajar la version compatible con en Chrome que tengo
  * Crear un archivo .py dentro del proyecto en Visual Studio Code
  * Hacer el import webdriver: from selenium import webdriver
  * Despues instanciar el webdriver:  driver = webdriver.Chrome("C:/Users/paula/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
  * Cuando no encuentra la ruta, podemos ponerla dentro de la variable de entorno en path( he probado he funciona muy bien)
  * 

**************************************************************************************************************************************
