# ===========================================================================
# Importaciones de clases y librerias necesarias en este archivo main
# ===========================================================================

# Region -  Importaciones de archivos o librerias
from controller.Log import Log
from controller.Impresor import Impresor
from content.Selenium import Selenium
# Endregion - Importaciones de archivos o librerias

# ===========================================================================
# VARIABLES GLOBALES - LOCALES - INICIALIZACION DE OBJETOS
# ===========================================================================

# Region - Instancia de clases de archivos importado
logger = Log()
consola = Impresor()
bot = Selenium()
# Endregion - Instancia de clases de archivos importado

def main():
    try: 
        consola.imprimirInicio("Nombre De La Automatización")
        logger.registroInicioProcesos()
        consola.imprimirProceso("Inicio de ejecución del proceso")
        logger.registrarLogProceso("Inicio de ejecución del proceso")
        
        # Region - Cuerpo de la automatización
        bot.iniciarBot()
        # Endregion - Cuerpo de la automatización
                
        consola.imprimirFinal()
        logger.registroFinalProcesos()
    except Exception as e:
        logger.registrarLogEror(f"Except del main: {e}", "Ejecución de Main")
        consola.imprimirError(f"Ocurrió un error en la ejecución: {e}")
    
# Metodo para ejecución del Script, invocando la función main()    
if __name__ == '__main__':
    main()