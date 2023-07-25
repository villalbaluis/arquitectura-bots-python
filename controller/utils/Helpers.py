# region Importando librerias o clases necesarias
import os
import json
from PIL import ImageTk, Image
import pathlib
import zipfile
import shutil
import glob
from pathlib import Path
# endregion Importando librerias o clases necesarias

# region Instanciar Objetos y variables Globales

# Obtención del path absoluta del proyecto
relativePath = os.getcwd()
# Obtención del user name de la maquina de ejecución
usuarioMaquinaActual = os.getlogin()

# endregion Instanciar Objetos y variables Globales

class Helpers:
    """
        Helpers
        ======= 
        La clase se encargará de entregar distinto metodos,
        cada uno encargado de retornar un valor, modificar un elemento,
        obtener una ruta, o todas aquellas utilidades que puedan ser usadas
        en cualquier lugar necesario dentro de la aplicación
        ## Usos
        - Obtener rutas desde el archivo de configuración
        - Obtener rutas del equipo donde se esta desarrollando.
        - Generar interacciones con Tkinter en la GUI.
    """
    
    # Constructor de la clase
    def __init__(self):
        self.__routeConfig = relativePath + "/config.json"
        self.__initial_count = 0
    
    # Region Metodos usados en la clase
    
    # Obtiene una ruta del archivo config concatenado con el path del proyecto
    def getRoutes(self, key: str, value: str):
        """
            Se le pasa la llave del archivo config, y el value del objeto
            para que retorne el path concatenado con la ruta del proyecto
            - `Args:`
                - key (str): Nombre de la llave del archivo config
                - value (str): Nombre de la llave dentro del objeto del config
            - `Returns:`
                fullpath (str): Ruta completa del proyecto más el valor encontrado
        """
        with open(self.__routeConfig, 'r') as file: 
            config = json.load(file)
            if config[key][value] == "":
                file.close()
                return
            else:
                route = str(config[key][value])
                file.close()
        
        fullpath = relativePath + route
        return fullpath
    
    # Obtiene el valor de la key dada del config
    def getValue(self, key: str, value: str):
        """
            Se le pasa la key y el name value del elememto
            dentro del config.json, de manera que solo retornaria
            el valor del objeto buscado
            - `Args:`
                - key (str): Nombre de la llave del archivo config
                - value (str): Nombre del value del atributo
            - `Returns:`
                data (str): Valor de la propiedad buscada en el JSON
        """
        with open(self.__routeConfig, 'r') as file: 
            config = json.load(file)
            if config[key][value] == "":
                file.close()
                return
            else:
                data = str(config[key][value])
                file.close()
        # Validación de str por defecto, y reemplazo por el usuario actual
        if("USUARIOXYZ" in data):
            data = data.replace("USUARIOXYZ", usuarioMaquinaActual)
        return data
    
    # Cuenta el total de registros de un dataframe dado
    def countRecordsDataframe(self, totalcount):
        aloneRows = totalcount.split(",")
        total = str(aloneRows[0]).replace("(", "")
        return total
    
    # Cuenta el total de carpetas dentro de un directorio
    def countFolder(self, ruta):
        """
            Toma un directorio de un path completo, retorna la cantidad
            total de directorios encontrados dentro de la ruta dada.
            - `Args:`
                - ruta (str): Ruta del directorio raíz
            - `Returns:`
                total (int): Cantidad de subdirectorios
        """
        self.__initial_count = 0
        for path in pathlib.Path(ruta).iterdir():
            if path.is_dir():
                self.__initial_count += 1
                
        return self.__initial_count
    
    # Cuenta la cantidad de archivos según extensión
    def countFilesExtension(self, path, extension):
        cantidadArchivos = len(glob.glob1(path, f"{extension}"))
        return cantidadArchivos
    
    # Metodo para extraer un archivo zip sin duplicarse
    def extractZip(self, rutaZip):
        """
            Toma una ruta absoluta de un archivo comprimido en ".zip" para
            luego descomprimir el archivo, borrar el ".zip" original
            y retornar la ruta de la carpeta extraida
            - `Args:`
                - rutaZip (str or pathType): Ruta del archivo ".zip"
            - `Returns:`
                ruta_extraida (str or pathType): Ruta de la carpeta descomprimida
        """
        rutaConfig = rutaZip.split('\\')
        deleteFile = rutaConfig[-1]
        deleteZip = deleteFile.replace(".zip", "")
        ruta_extraccion = rutaZip.replace(deleteFile, "")
        ruta_extraida = ruta_extraccion + "\\" + deleteZip
        try:
            shutil.rmtree(ruta_extraida)
        except OSError as e:
            print("No hay ruta para eliminar " + str(e))
        archivo_zip = zipfile.ZipFile(rutaZip, "r")
        try:
            archivo_zip.extractall(path=ruta_extraccion)
        except Exception  as e:
            print(str(e))
        archivo_zip.close()
        return ruta_extraida
    
    # Obtención de la carpeta documents independiente del usuario que ejecuta
    def pathDocumentsUser(self):
        if os.name == 'nt':
            pathDocs = Path(os.environ['USERPROFILE']) / 'Documents'
        rutaDocuments = pathDocs.resolve()
        return rutaDocuments
        
    # Metodo para realizar la validacion del destino
    def ValidateDestiny(self, ruta):
        cont = 0
        dir = ruta
        for f in os.listdir(dir):
            cont += 1
        return cont

    # Region - Metodos de utilidad para uso de interfaz gráfica
    
    # Toma una pantalla de Tkinter y la centra en la pantalla del usuario
    def centerWindows(self, windows, height, withs):
        anchoPantalla = windows.winfo_screenwidth()
        largoPantalla = windows.winfo_screenheight()
        x = int((anchoPantalla/2) - (withs/2))
        y = int((largoPantalla/2) - (height/2))
        return windows.geometry(f"{withs}x{height}+{x}+{y}")
    
    # Nos permite cargar una imagen de forma dinamica
    def getImage(self, key, size):
        """
            Carga una imagen de un ruta dada, y la recorta al tamaño dado
            - `Args:`
                - key (str): Path o key value de la imagen
                - size (tuple): Tupla de medidas (width, height)
            - `Returns:`
                (Objecto TkinterImage): Objeto de ImageTk con la imagen obtenida
        """
        image = Image.open(self.getRoutes(key, "Value")).resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)  
    
    # Permite modificar el valor de un elemento GUI
    def SetInfoElement(self, element, value):
        """
            Toma un objeto gráfico de Tkinter, modifica su valor
            y luego deshabilita el objeto
            - `Args:`
                - element (tkinter object): Elemento de la interfaz gráfica a modificar
                - value (str): Valor nuevo a mostrar en el elemento
        """
        element.configure(state = 'normal')
        element.delete(0, "end")
        element.insert(0, str(value))
        element.configure(state = 'disabled')
    
    # Nos permite habilitar un elemento del GUI
    def setEnableItem(self, element):
        element.configure(state='normal')

    # Nos permite deshabilitar un elemento del GUI
    def setDisabledItem(self, element):
        element.configure(state='disabled')
        
    # Endregion - Metodos de utilidad para uso de interfaz gráfica
        
    # Endregion Metodos usados en la clase
    