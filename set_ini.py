#       script PARA CREAR UN .INI O ARCHIVO DE CONFIGURACION
import configparser
#configparser, es un modulo que viene por default en python
# parsea una configuracion para luego grabarla en un archivo
# al cual le daremos la extencion a gusto, en este caso .ini

#declaro una variable
configuracion = configparser.ConfigParser()

#le doy formato. Se usa esta variable (configuracion)porque 
# aqui estamos parseando el archivo a crear

#creamos 2 secciones, general y paginas
#En general va el navegador a usar y la direccion de su driver
#En paginas, van aquellas paginas en las que haré pruebas
configuracion['General'] = {'Firefox' : 'C:\DriverSelenium\Firefox\geckodriver.exe' }
configuracion['Paginas'] = {'page' : 'https://gerabarud.github.io/is3-calculadora/'}

#abrimos el archivo para cargar la informacion y que se guarde, 'w' significa que va a grabar
with open('configCalc.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig)
