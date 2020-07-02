import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
"""Clase de utilidades

Clase con todos los metodos y utilidades necesarias para llevar a cabo
el proceso de testing facilitando el ahorro y reutilizacion de codigo (evitando redundancias) como 
asi tambien una clase de testeo mas limpia, ordenada y rapida de construir.
"""
class UtilidadesTestCalc:
        #funcion de espera corta
        def wait(self, SleepTime = 3):
            time.sleep(SleepTime)

        #funcion de espera larga
        def longwait(self, SleepTime = 6):
            time.sleep(SleepTime)
        def scroll_it(self, driver):
            """Hace scroll hasta el final de la pagina

            Parametros:\n
            driver -- variable con la instancia del navegador
            """
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


        def cargar_First_and_Second(self, driver, firstN, secondN):
            """Carga los campos First Number y Second Number

            Parametros:\n
            driver -- variable con la instancia de el navegador \n
            firstN -- valor a cargar en el campo First Number \n
            secondN -- valor a cargar en el campo Second Number
            """
            campo1 = driver.find_element_by_id("number1Field")
            campo1.send_keys(firstN)
            campo2 = driver.find_element_by_id("number2Field")
            campo2.send_keys(secondN)
            

        def elegir_operacion(self, driver, indexOp):
            """Controla el select y elige la operacion deseada

            Parametros:\n
            driver -- variable con la instancia del navegador\n
            indexOp -- Valor de 0 a n, el cual corresponde a la posicion de la operacion en el selector. 
                     Las posiciones comienzan en 0.
            """
            operacion = Select(driver.find_element_by_id("selectOperationDropdown"))
            operacion.select_by_index(indexOp)
        
        def elegir_operacion_Y_click_Boton_Calcular(self,driver,indexOp):
            UtilidadesTestCalc.elegir_operacion(self,driver,indexOp)
            UtilidadesTestCalc.click_Boton_Calcular(self,driver)
        
        def cargar_y_elegirOp(self, driver, firstN, secondN, indexOp):
            """ Carga los campos First Number y Second Number con los valores pasados por parametro
            luego determina la operacion a realizar mediante el index del atributo select

            Parametros:\n
            driver -- variable con la instancia del navegador\n
            firstN -- valor a cargar en el campo First Number\n
            secondN -- valor a cargar en el campo Second Number\n
            indexOp -- Valor de 0 a 4, el cual corresponde a la posicion de la operacion en el selector. 
                     Las posiciones comienzan en 0.
            """
            UtilidadesTestCalc.scroll_it(self,driver)
            UtilidadesTestCalc.cargar_First_and_Second(self,driver,firstN,secondN)
            UtilidadesTestCalc.elegir_operacion(self,driver,indexOp)
        
        def ejecucion_completa(self, driver, build_value, firstN, secondN, indexOp):
            """ Carga los campos First Number y Second Number con los valores pasados por parametro
            luego determina la operacion a realizar mediante el index del atributo select

            Parametros:\n
            driver:: variable con la instancia del navegador\n
            (string)build_value:: valor de "1" a "9" que indicara el build a utilizar,
                     valor "Prototype" será igual a Prototype \n
            firstN::  valor a cargar en el campo First Number\n
            secondN:: valor a cargar en el campo Second Number\n
            indexOp:: Valor de 0 a 4, el cual corresponde a la posicion de la operacion en el selector. 
                     Las posiciones comienzan en 0.
            """
            
            UtilidadesTestCalc.scroll_it(self,driver)
            UtilidadesTestCalc.elegir_build(self,driver,build_value)           
            UtilidadesTestCalc.cargar_First_and_Second(self,driver,firstN,secondN)
            UtilidadesTestCalc.elegir_operacion(self,driver,indexOp)

            UtilidadesTestCalc.click_Boton_Calcular(self,driver)
            UtilidadesTestCalc.wait(self)

        def click_Boton_Calcular(self, driver):
            """Acciona el boton calcular
            Parametros:\n
            driver -- variable con la instancia del navegador\n
            """
            boton = driver.find_element_by_id("calculateButton")
            boton.click()
        def click_Boton_Clear(self,driver):
            """Acciona el boton clear
            Parametros:\n
            driver -- variable con la instancia del navegador\n
            """
            boton = driver.find_element_by_id("clearButton")
            boton.click()
        
        
        def click_Boton_Calcular_solo_resultados_enteros(self,driver):
            """Acciona el boton calcular y el check de solo resultados enteros

            Parametros:\n
            driver -- variable con la instancia del navegador\n
            """
            UtilidadesTestCalc.click_Boton_Calcular(self,driver)
            check_Solo_Enteros = driver.find_element_by_id("integerSelect")
            check_Solo_Enteros.click()
        
        def check_enteros(self,driver):
            """Activa/Desactiva el check de "solo enteros"
            Parametros:\n
            driver -- variable con la instancia del navegador\n
            """
            check_Solo_Enteros = driver.find_element_by_id("integerSelect")
            check_Solo_Enteros.click()

        def elegir_build(self,driver,build_value):
            """Permite elegir el buid a utilizar"
            
            Parametros:\n
            (string)build_value:: valor de "1" a "9" que indicara el build a utilizar,
                     valor "Prototype" será igual a Prototype \n
            """
            build = Select( driver.find_element_by_id("selectBuild") )
            build.select_by_visible_text(build_value)

        #def tripleTest_srm(self, driver, build_value, firstN, secondN,nerror):
         #   """ Carga los campos First Number y Second Number con los valores pasados por parametro
          #  luego determina la operacion a realizar mediante el index del atributo select
#
 #           Parametros:\n
  #          driver:: variable con la instancia del navegador\n
   #vv         (string)build_value:: valor de "1" a "9" que indicara el build a utilizar,
      ##               valor "Prototype" será igual a Prototype \n
        #    firstN::  valor a cargar en el campo First Number\n
         #   secondN:: valor a cargar en el campo Second Number\n
          #  
           # """
          # print("suma")
         #   UtilidadesTestCalc.ejecucion_completa(self,driver, "Prototype", firstN,secondN,0)
          #  assert driver.find_element_by_id("errorMsgField").text == "Number " +nerror+ " is not a number"
           # 
            #print("resta") 
            #UtilidadesTestCalc.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
            #assert driver.find_element_by_id("errorMsgField").text == "Number " +nerror+ " is not a number"
            
            #print("multiplicacion")
            #UtilidadesTestCalc.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
            #assert driver.find_element_by_id("errorMsgField").text == "Number " +nerror+ " is not a number"
    

        


            


            

