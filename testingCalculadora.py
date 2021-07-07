import unittest
import configparser 
#configparser es necesario para el archivo de configuracion creado por mi para inicializar el test
from utilidadesTestCalc import UtilidadesTestCalc 
#clase creada por mi para mejor mantenimiento y  reutilizacion de codigo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import dataCalc #clase con los datos de entrada
import operator

d = dataCalc
u = UtilidadesTestCalc

build_value = "Prototype"

class calculadoraTesting(unittest.TestCase):

    def setUp(self):
         print("Preparando el contexto\n")
         configuracion = configparser.ConfigParser()
         configuracion.read('configCalc.ini')
         configuracion.sections()
         navegador = configuracion['General']['Firefox']
         self.page = configuracion['Paginas']['page']
         self.driver = webdriver.Firefox(executable_path=navegador)
        
         
    
    
    def test_limite_de_caracteres(self): #1
        print("Caso de Prueba nro 1")
        driver = self.driver
        driver.get(self.page)
                
        #wait()
        firstNumber = driver.find_element_by_id("number1Field")
        print("El maximo de caracteres que soporta es "+ firstNumber.get_attribute('maxlength'))

    def test_operAritm_acepta_una_Letra_distinta_de_e(self): #2
        print("Caso de Prueba nro 2")
        driver = self.driver
        driver.get(self.page)
        u.scroll_it(self,driver)
        u.cargar_y_elegirOp(self,driver,d.srm_First_number[1],d.srm_Second_number[1],0)
        u.click_Boton_Calcular(self,driver)      
        u.wait(self,1)#cuando se quiera se puede dar menos tiempo
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_operAritm_acepta_una_Letra_distintas_de_e_v2(self): #3
        print("Caso de Prueba nro 3")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[2],d.srm_Second_number[2],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_operAritm_acepta_una_Letra_distintas_de_e_v3(self):
        print("Caso de Prueba nro 4") #4
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[3],d.srm_Second_number[3],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
    
    def test_conjuntoDeLetras_distintasDe_e(self):
        print("Caso de Prueba nro 5")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[4],d.srm_Second_number[4],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_conjuntoDeLetras_distintasDe_e_v2(self):
        print("Caso de Prueba nro 6")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[5],d.srm_Second_number[5],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_conjuntoDeLetrasYnros_distintasDe_e(self):
        print("Caso de Prueba nro 7")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[6],d.srm_Second_number[6],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_conjuntoDeLetrasYnros_distintasDe_e_v2(self):
        print("Caso de Prueba nro 8")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[7],d.srm_Second_number[7],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
    
    def test_conjuntoDeNrosY_simbolosInvalidos(self):
        print("Caso de Prueba nro 9")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[8],d.srm_Second_number[8],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"

    def test_conjuntoDeNrosY_simbolosInvalidos_v2(self):
        print("Caso de Prueba nro 10")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[9],d.srm_Second_number[9],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
    
    def test_nros_con_Simbolo_coma(self):
        print("Caso de Prueba nro 11")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[10],d.srm_Second_number[10],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_nros_con_Simbolo_coma_v2(self):
        print("Caso de Prueba nro 12")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[11],d.srm_Second_number[11],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
    
    def test_conjunto_de_simbolosInvalidos_letras_coma_y_enteros(self):
        print("Caso de Prueba nro 13")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[12],d.srm_Second_number[12],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 1 is not a number"
    
    def test_conjunto_de_simbolosInvalidos_letras_coma_y_enteros_v2(self):
        print("Caso de Prueba nro 14")
        driver = self.driver
        driver.get(self.page)
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[13],d.srm_Second_number[13],0)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        assert driver.find_element_by_id("errorMsgField").text == "Number 2 is not a number"
    
    def test_valores_decimales_usando_punto(self):
        print("Caso de Prueba nro 15")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")

        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[14],d.srm_Second_number[14],0)
        self.assertEqual(6, int(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(1, int(resultado.get_attribute('value')))
        u.wait(self)
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(8.75, float(resultado.get_attribute('value')))
    
    def test_valores_notacion_cientifica(self):
        print("Caso de Prueba nro 16")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[15],d.srm_Second_number[15],0)
        self.assertEqual(operator.add(float(d.srm_First_number[15]),float(d.srm_Second_number[15])), float(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(operator.sub(float(d.srm_First_number[15]),float(d.srm_Second_number[15])), float(resultado.get_attribute('value')))
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(operator.mul(float(d.srm_First_number[15]),float(d.srm_Second_number[15])), float(resultado.get_attribute('value')))
    
    def test_valores_negativos(self):
        print("Caso de Prueba nro 17")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[16],d.srm_Second_number[16],0)
        self.assertEqual(operator.add(int(d.srm_First_number[16]),int(d.srm_Second_number[16])), int(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(operator.sub(int(d.srm_First_number[16]),int(d.srm_Second_number[16])), int(resultado.get_attribute('value')))
        u.wait(self,0.5)
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(operator.mul(int(d.srm_First_number[16]),int(d.srm_Second_number[16])), int(resultado.get_attribute('value')))

    def test_decimales_negativos_notacion_cientifica(self):
        print("Caso de Prueba nro 18")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[17],d.srm_Second_number[17],0)
        self.assertEqual(operator.add(float(d.srm_First_number[17]),float(d.srm_Second_number[17])), float(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(operator.sub(float(d.srm_First_number[17]),float(d.srm_Second_number[17])), float(resultado.get_attribute('value')))
        
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(str(int(operator.mul(float(d.srm_First_number[17]),float(d.srm_Second_number[17])))), resultado.get_attribute('value'))
    

    def test_vacio_1er_campo(self):
        print("Caso de Prueba nro 19")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[18],d.srm_Second_number[18],0)
        self.assertEqual(8, int(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(-8, int(resultado.get_attribute('value')))
        u.wait(self,0.5)
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(0, int(resultado.get_attribute('value')))
    
    def test_vacio_2do_campo(self):
        print("Caso de Prueba nro 20")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[19],d.srm_Second_number[19],0)
        self.assertEqual(8, int(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(8, int(resultado.get_attribute('value')))
        u.wait(self)
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(0, int(resultado.get_attribute('value')))
    
    def test_prop_elem_neutro_sum_sub(self):
        print("Caso de Prueba nro 21")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[20],d.srm_Second_number[20],0)
        self.assertEqual(operator.add(int(d.srm_First_number[20]),int(d.srm_Second_number[20])), int(resultado.get_attribute('value')))
        
        print("resta")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,1)
        self.assertEqual(operator.sub(int(d.srm_First_number[20]),int(d.srm_Second_number[20])), int(resultado.get_attribute('value')))
        
    def test_prop_elem_neutro_mul_div(self):
        print("Caso de Prueba nro 22")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")

        print("multiplicacion")
        u.ejecucion_completa(self,driver, build_value, d.srm_First_number[21],d.srm_Second_number[21],2)
        self.assertEqual(operator.mul(int(d.srm_First_number[21]),int(d.srm_Second_number[21])), int(resultado.get_attribute('value')))

        print("division")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,3)
        self.assertEqual(operator.mul(int(d.srm_First_number[21]),int(d.srm_Second_number[21])), int(resultado.get_attribute('value')))

    
    def test_apretarCalcular_cincoVeces_op_suma(self):
        print("Caso de Prueba nro 23")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")

        u.cargar_y_elegirOp(self,driver,d.srm_First_number[22],d.srm_Second_number[22],0)
        for x in range (5):
            u.click_Boton_Calcular(self,driver)

        self.assertEqual(15,int(resultado.get_attribute('value')))
    
    def test_prop_conmutativa_ida(self):
        print("Caso de Prueba nro 1 de sm")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.sm_First_number[0],d.sm_Second_number[0],0)
        self.assertEqual(9, int(resultado.get_attribute('value')))
                
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(20, int(resultado.get_attribute('value')))

    def test_prop_conmutativa_vuelta(self):
        print("Caso de Prueba nro 2 de sm")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("suma")
        u.ejecucion_completa(self,driver, build_value, d.sm_First_number[1],d.sm_Second_number[1],0)
        self.assertEqual(9, int(resultado.get_attribute('value')))
                
        print("multiplicacion")
        u.elegir_operacion_Y_click_Boton_Calcular(self,driver,2)
        self.assertEqual(20, int(resultado.get_attribute('value')))

    def test_div_por_cero(self):
        print("Caso de Prueba nro 1 de div")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("division por 0")
        u.ejecucion_completa(self,driver, build_value, d.div_First_number[0],d.div_Second_number[0],3)
        assert driver.find_element_by_id("errorMsgField").text == "Divide by zero error!"
        
    def test_cero_div_cualquier_nro(self):
        print("Caso de Prueba nro 2 de div")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("0 dividido por any")
        u.ejecucion_completa(self,driver, build_value, d.div_First_number[1],d.div_Second_number[1],3)
        self.assertEqual(0, int(resultado.get_attribute('value')))
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
    def test_caracteres_alfabeticos(self):
        print("Caso de Prueba nro 1 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("alfabeticos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[0],d.concat_Second_number[0],4)
        self.assertEqual(d.R_answer[0], resultado.get_attribute('value'))

    def test_caracteres_silabicos(self):
        print("Caso de Prueba nro 2 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("silabicos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[1],d.concat_Second_number[1],4)
        self.assertEqual(d.R_answer[1], resultado.get_attribute('value'))
    
    def test_caracteres_sinograficos(self):
        print("Caso de Prueba nro 3 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("sinograficos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[2],d.concat_Second_number[2],4)
        self.assertEqual(d.R_answer[2], resultado.get_attribute('value'))
    
    def test_emojis_y_dibujos_unicode(self):
        print("Caso de Prueba nro 4 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("alfabeticos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[3],d.concat_Second_number[3],4)
        self.assertEqual(d.R_answer[3], resultado.get_attribute('value'))

    def test_combinacion_de_todo(self):
        print("Caso de Prueba nro 5 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("alfabeticos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[4],d.concat_Second_number[4],4)
        self.assertEqual(d.R_answer[4], resultado.get_attribute('value'))
    
    def test_cumple_prop_elem_neutro_Concat(self):
        print("Caso de Prueba nro 6 de concat")
        driver = self.driver
        driver.get(self.page)
        resultado = driver.find_element_by_id("numberAnswerField")
        
        print("alfabeticos")
        u.ejecucion_completa(self,driver, build_value, d.concat_First_number[5],d.concat_Second_number[5],4)
        self.assertEqual(d.R_answer[5], resultado.get_attribute('value'))

    
    


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
       
