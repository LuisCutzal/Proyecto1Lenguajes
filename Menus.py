import os
import sys
import time
import Funciones
import Cargas_masivas
def MenuInicio():
    while True:
        os.system('cls')
        print("*****************************")
        print("*****************************")
        print ("Menú Principal")
        print ("\t1 - Modulo AFD: ")
        print ("\t2 - Modulo de Gramáticas Regulares: ")
        print ("\t3 - Acerca de...: ")
        print ("\t4 - Salir ")
        print("*****************************")
        print("*****************************")
        opcionMenu = input("Escriba uno de los 4 números a  la que quiere ingresar: ")
        if opcionMenu == "1":
            print("Ha elegido Modulo AFD")
            print("espere...")
            time.sleep(2)
            SubMenu1()
        elif opcionMenu == "2":
            print("Ha elegido Modulo de Gramáticas Regulares:")
            print("espere...")
            time.sleep(2)
            SubMenu2()
        elif opcionMenu=="3":
            print("espere...")
            Acerca()
        elif opcionMenu=="4":
            sys.exit(0)    
        else:
            print("Ha pusaldo una tecla incorrecta, vuelva a intentarlo")
            time.sleep(2)

def Acerca():
    os.system('cls')
    print("---------------Datos del Curos------------------")
    print("Lenguajes Fromales y de Programacion")
    print("Ingeniera: Zulma Aguirre")
    print("Auxiliar: Danilo Urías Coc")
    print("Seccion: B")
    input("Precione cualquier tecla para regresar al Menú anterior: ")

def SubMenu1(): #------------------------------modulo AFD--------------------------------------
    while True:
        os.system('cls')
        print("*****************************")
        print ("MODULO AFD")
        print ("\t1 - Crear AFD: ")
        print ("\t2 - Cargar Archivo: ")
        print ("\t3 - Evaluar Cadena: ")
        print ("\t4 - Guardar AFD en archivo: ")
        print ("\t5 - Guardar Gramática en archivo: ")
        print ("\t6 - Generar Gramática Regular: ")
        print ("\t7 - Regresar:")
        print("*****************************")
        opcionSub = input("Escriba uno de los 6 números a  la que quiere ingresar: ")
        if opcionSub== "1":
            print("Eligio Crear AFD")
            print("espere...")
            time.sleep(1)
            Funciones.AgregarAFD()
        elif opcionSub == "2":
            print("Eligio Cargar Archivo")
            print("espere...")
            time.sleep(1)
            Cargas_masivas.CargarArchivoAFD()
        elif opcionSub=="3":
            print("Eligio Evaluar Cadena")
            print("espere...")
            time.sleep(1)
            Funciones.EvaluarCadena()
        elif opcionSub=="4":
            input("Guardar AFD")
        elif opcionSub == "5":
            input("Guardar Gramática")
        elif opcionSub =="6":
            input("Generar Gramatica")
        elif opcionSub == "7":
            print("regresando...")
            time.sleep(1)
            break    
        else:
            print("Ha pusaldo una tecla incorrecta, vuelva a intentarlo")
            time.sleep(2)


def SubMenu2(): #------------------------------modulo Gramáticas Regulares--------------------------------------
    while True:
        os.system('cls')
        print("*****************************")
        print ("MODULO AFD")
        print ("\t1 - Crear Gramática: ")
        print ("\t2 - Cargar Archivo: ")
        print ("\t3 - Evaluar Cadenas: ")
        print ("\t4 - Eliminar Recursividad por la Izquierda: ")
        print ("\t5 - Guardar AFD en archivo: ")
        print ("\t6 - Generar Reporte Gramática Regular: ")
        print ("\t7 - Regresar:")
        print("*****************************")
        opcionSub = input("Escriba uno de los 6 números a  la que quiere ingresar: ")
        if opcionSub== "1":
            Funciones.AgregarGramatica()
        elif opcionSub == "2":
            Cargas_masivas.CargarArchivoGramatica()
        elif opcionSub=="3":
            input("Evaluar")
        elif opcionSub=="4":
            input("Eliminar")
        elif opcionSub == "5":
            input("Guardar AFD")
        elif opcionSub =="6":
            input("Generar Reporte")
        elif opcionSub == "7":
            print("regresando...")
            time.sleep(1)
            break    
        else:
            print("Ha pusaldo una tecla incorrecta, vuelva a intentarlo")
            time.sleep(2)


#----------------------main--------------------
def main():
    print("------------Lenguajes Formales y de Programacion-----------")
    print ("Seccion: B")
    print ("Carné: 201700841")
    input("presione cualquier tecla para iniciar el programa: ")
    MenuInicio()

if __name__ == "__main__":
    main()