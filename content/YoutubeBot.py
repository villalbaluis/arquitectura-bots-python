# region Importando librerias o clases necesarias
from time import sleep
from controller.Log import Log
from content.Selenium import Selenium
from controller.Impresor import Impresor
from selenium.webdriver.common.by import By
from controller.utils.KeyMouse import KeyMouse
from controller.utils.Configurations import Configurations
# endregion Importando librerias o clases necesarias

# ===========================================================================
# VARIABLES GLOBALES - LOCALES - INICIALIZACION DE OBJETOS
# ===========================================================================
# region - Instancia de clases de archivos importado
logger = Log()
mouse = KeyMouse()
consola = Impresor()
selenium = Selenium()
configuration = Configurations()
# endregion - Instancia de clases de archivos importado

class YoutubeBot:
    # Constructor de clase
    def __init__(self):
        """
            Constuctor de la clase, encargado de generar 
            las variables o instancias de metodos que serán
            necesarias dentro de la clases
        """
        self.__driver = selenium.retornarDriver()

    # region Metodos
    # Inicializador de proceso para el bot de youtube
    def iniciarBotYoutube(self):
        """
            Metodo encargado del llamado de las funciones
            que harán el procesamiento del bot dentro de
            la clase.
            - Se abrirán distintas páginas a través del metodo.
            - Se llevará una traza de inicio y fin
        """
        self.__driver.maximize_window()
        sleep(1)
        consola.imprimirProceso("Inicio de marioneta")
        logger.registrarLogProceso("Inicio de marioneta")
        self.agregarAdblock()
        self.buscarCancion1()
        self.buscarCancion2()
        self.buscarCancion3()
        self.__driver.quit()
        consola.imprimirProceso("Bot Finalizado")
        logger.registrarLogProceso("Bot Finalizado")
    
    
    def agregarAdblock(self):
        """
            Metodo encargado de quitar los anuncios encontrados
            dentro del video que se esta reproduciendo.\n
            Simularia un comportamiento de movimiento de mouse 
            para generar el click en la pantalla.
        """
        consola.imprimirProceso("Agregando adBlock")
        logger.registrarLogProceso("Agregando adBlock")
        self.__driver.get(configuration.getConfigValue("urls","adblock"))
        sleep(3)
        add = self.__driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[1]/section[1]/div/header/div[3]/div/div/a')
        sleep(2)
        add.click()
        sleep(2)
        mouse.moverMouse((1700,350))
        sleep(2)
        mouse.singleClick()
        sleep(5)

    # Region - Metodos encargados de la busqueda e interacción con la página
    def buscarCancion1(self):
        consola.imprimirProceso("Ejecucion de primer cancion")
        logger.registrarLogProceso("Ejecucion de primer cancion")
        self.__driver.execute_script("window.open('');")
        self.__driver.switch_to.window(self.__driver.window_handles[1])
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube1"))
        sleep(3)
        btnPremium = self.__driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        sleep(3)
        btnPremium.click()
        sleep(3)
        mouse.moverMouse((1080,810))
        sleep(3)
        mouse.singleClick()
        sleep(int(configuration.getConfigValue("time","videoTime")))

    def buscarCancion2(self):
        consola.imprimirProceso("Ejecucion de segunda cancion")
        logger.registrarLogProceso("Ejecucion de segunda cancion")
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube2"))
        sleep(3)
        mouse.moverMouse((1220,810))
        sleep(3)
        mouse.singleClick()
        sleep(int(configuration.getConfigValue("time","videoTime")))
    
    def buscarCancion3(self):
        consola.imprimirProceso("Ejecucion de tercera cancion")
        logger.registrarLogProceso("Ejecucion de tercera cancion")
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube3"))
        sleep(3)
        mouse.moverMouse((1220,810))
        sleep(3)
        mouse.singleClick()
        sleep(int(configuration.getConfigValue("time","videoTime")))
    # Region - Metodos encargados de la busqueda e interacción con la página
    
    # endregion
        