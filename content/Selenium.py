# region - Importaciones de clases y librerias
import os
from time import sleep
from controller.Log import Log
from selenium import webdriver
from controller.Impresor import Impresor
from controller.utils.Helpers import Helpers
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from controller.utils.Configurations import Configurations
# endregion - Importaciones de clases y librerias


# region - Inicialización de clases o variables globales
logger = Log()
help = Helpers()
consola = Impresor()
configuration = Configurations()
# endregion - Inicialización de clases o variables globales

class Selenium:
    """
        Selenium
        ========
        Esta clase se encargará unicamente de crear el 
        llamado del GeckoDriver, encargado de la gestión
        del bot en las automatizaciones web.
        ### Aspectos a considerar:
        - Esta clase solo retorna el `driver`, no los metodos de Selenium.
        - Para usar metodos de Selenium, se instancia en la clase que lo llame.
        - Existen dos formas de instanciar el Driver, la forma uno es usada
        en la `versión 4.10 de Selenium`, y la forma 2, en versiones anteriores.
    """
    def __init__(self):
        """
            Se inicializa los atributos de la clase Robot
            Para la plantilla se deja inicializado el driver en el metodo init
            pero se puede inicializar y modificar a medida del requerimiento
            - Usaremos selenium con `Firefox` usando el GeckoDriver
                para la automatización web
            - Usaremos el argumento `"--disable-blink-features=AutomationControlled"`
                para prevenir la detección del bot como automatización
        """        
        # DESCOMENTAR LAS SIGUIENTES LINEAS SEGÚN LA NECESIDAD DEL REQUERIMIENTO
        
        # Forma 1: Iniciar las variables del Driver, funcional con Selenium v4.10
        self.opcionesDriver = Options() # Se inicializan las opciones del driver para Firefox
        self.opcionesDriver.add_argument('--disable-blink-features=AutomationControlled')
        # Se inicializa el servicio en la ruta del GeckoDriver
        self.servicePath = Service(os.getcwd() + configuration.getConfigValue("drivers","GeckoDriver")) 

        # Forma 2: Iniciar las variables del Driver, funcional con Selenium v4.9 o menores
        # self.executablePath = help.getRoutes("GeckoDriver", "Value")
        

    # region Metodos usados para la automatización con Selenium
    
    def retornarDriver(self):
        """
            Metodo encargado de inicializar el GeckoDriver para 
            el uso de selenium en la automatización web
            ## `Uso`
            - Retornará la instancia del driver, para que al ser llamado
            desde otro archivo, pueda usarse la interacción web a través
            de Firefox.
            ## `Nota`
            - En caso de necesitar otro metodo de la clase Selenium, se deberá
            importar dentro del archivo que llamo el Driver, y no en este archivo.
        """
        try:
            # Instancia del driver de la Forma 1 (Descomentar las variables del init)
            driver = webdriver.Firefox(service = self.servicePath, options = self.opcionesDriver)            
            sleep(2)

            # Instancia del driver de la Forma 2 (Descomentar la linea de la Forma 2 del Init)
            # driver = webdriver.Firefox(executable_path = self.servicePath)
            
            # Comentar o eliminar el Driver que no se usará según la versión y forma usadada.
            consola.imprimirProceso("Instancia del objeto driver")
            logger.registrarLogProceso("Instancia del objeto driver")
            return driver
        except Exception as e:
            consola.imprimirError(str(e))
            logger.registrarLogEror(f"Inicialización del GeckoDriver, error: {e}", "retornarDriver")
            return None
        
    # endregion Metodos usados para la automatización con Selenium
    