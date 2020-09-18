import codecs
from Automatas import *
from io import open
import time
import os
import sys
import csv
global todo
todo=list()
#todo.append(Automatas)
global estado
estado=list()
def Agregar():
    nombre =input("Ingrese el nombre del AFD: ")
    todo.append(Automatas(nombre))
    """if todo:
        for x in range(len(todo)):
            if nombre==todo[x].getNombreAFD() and todo[x].getTipo()=="AFD":
                input("Ya existe un AFD con el mismo nombre:")
            else:
                todo.append(Automatas(nombre))
                print("el nombre es: " + todo[x].getNombreAFD())
                input("hola")
    else:
        input("Error, no entro a la condicion")"""
       

#---------ingresar estados------------
    ingreEstados=True
    while ingreEstados:
        estados=(input("Ingrese Estado del AFD: "))
        estadoIngresado = estados.upper() #hace que los valores ingresados se conviertan en Mayusculas
        #creacionEstado = Estados(estadoIngresado)
        condicion=input("¿Desea ingresar otro estado? [Y/N]: ")
        if condicion =="Y" or condicion =="y" or condicion=="Yes" or condicion =="si" or condicion=="s":
            creacionEstado = Estados(estadoIngresado)
            #estado.append(Estados(estadoIngresado))
            for a in range(len(todo)):
                #if nombre== Automatas(todo[a].getNombreAFD()) and Automatas(todo[a].getTipo())=="AFD":
                if nombre == todo[a].getNombreAFD()  and todo[a].getTipo() =="AFD": #ver 
                    if todo[a].getEstados():
                        banderaEstados=0
                        for otro in range(len(todo[a].getEstados())):
                            if estadoIngresado == todo[a].getEstados()[otro].getNombreEstado(): #no me aparece .getNombreEstado()
                                banderaEstados+=1
                        if banderaEstados==0:
                            todo[a].getEstados().append(creacionEstado)
                            #todo[a].getEstados().append(estadoIngresado)
                        else:
                            input("El estado ya existe, no puede haber dos estados con el mismo nombre: ")
                    else:
                        creacionEstado.setEstadoFinal(True)
                        todo[a].getEstados().append(creacionEstado)
                        
                        #todo[a].getEstados().append(estadoIngresado)
            ingreEstados=True
        else: #no guardo nada ver, solo guardar un dato
            creacionEstado = Estados(estadoIngresado)
            ingreEstados=False


#-------------ingresar Alfabeto-----------------------
    ingreseAlfabeto=True
    while ingreseAlfabeto:
        alfabeto=input("Ingrese Caracter del Alfabeto del AFD: ")
        caracterIngresado = alfabeto.lower()
        condicion2=input("¿Desea ingresar otra letra? [Y/N]: ")
        if condicion2 =="Y" or condicion2 =="y" or condicion2=="Yes" or condicion2 =="si" or condicion2=="s":
            for a in range(len(todo)):
                if nombre==todo[a].getNombreAFD() and todo[a].getTipo()=="AFD":
                    if todo[a].getAlfabeto():
                        banderaAlfa=0
                        for otro2 in range(len(todo[a].getAlfabeto())):
                            if caracterIngresado== todo[a].getAlfabeto()[otro2]:
                                banderaAlfa+=1
                        if banderaAlfa==0:
                            todo[a].getAlfabeto().append(caracterIngresado)
                        else:
                            input("Caracter ingresado ya existe en el Alfabeto: ")
                    else:
                        todo[a].getAlfabeto().append(caracterIngresado)
            ingreseAlfabeto=True
        else:
            ingreseAlfabeto = False


#----------------ingresar estado inicial--------------
    inicial=input("Ingrese Estado Inicial del AFD: ")
    for buscaInicio in range(len(todo)):
        if nombre==todo[buscaInicio].getNombreAFD() and todo[buscaInicio].getTipo()=="AFD":
            if todo[buscaInicio].getEstados():
                for buscoNuevo in range(len(todo[buscaInicio].getEstados())):
                    if todo[buscaInicio].getEstados()[buscoNuevo].getNombreEstado() == inicial:
                        for a in range(len(todo[buscaInicio].getEstados())):
                            todo[buscaInicio].getEstados()[a].setEstadoInicio(False)
                        todo[buscaInicio].getEstados()[buscoNuevo].setEstadoInicio(True)
            else:
                input("El AFD no cuenta con un estado para volverlo estado inicial")


#------------ingresar Estados Aceptacion----------------
    ingresarAceptaciones=True
    while ingresarAceptaciones:
        estadosAceptacion=input("Ingrese los estados de Aceptacion del AFD: ")
        condicion3 = input("¿Desea ingresar otro Estado de Aceptacion? [Y/N]")
        if condicion3 =="Y" or condicion3 =="y" or condicion3=="Yes" or condicion3 =="si" or condicion3=="s":
            for a in range(len(todo)):
                if nombre==todo[a].getNombreAFD() and todo[a].getTipo()=="AFD":
                    if todo[a].getEstados():
                        for buscar in range(len(todo[a].getEstados())):
                            if todo[a].getEstados()[buscar].getNombreEstado()==estadosAceptacion:
                                todo[a].gtEstados()[buscar].setEstadoAceptacion(True)
                    else:
                        input("El AFD no cuenta con ningun Estado: ")
            ingresarAceptaciones=True
        else:
            ingresarAceptaciones=False


#---------------------ingresar transiciones----------------------
    ingresartransiciones=True
    while ingresartransiciones:
        transicion=input("Ingrese la Transicion del AFD: ")
        condicion4=input("¿Desea ingresar otra Transicion? [Y/N]")
        if condicion4 =="Y" or condicion4 =="y" or condicion4=="Yes" or condicion4 =="si" or condicion4=="s":
            primero = transicion.split(',')
            varios=primero[1].split(';')
            for i in range(len(todo)):
                if nombre==todo[i].getNombreAFD() and todo[i].getTipo()=="AFD":
                    ban1=0
                    ban2=0
                    ban3=0
                    ban4=0
                    inicial = None
                    final = None
                    for termi in range(len(todo[i].getAlfabeto())): #terminales varios[0] 
                        if varios[0]==todo[i].getAlfabeto()[termi]:
                            ban3+=1
                    for first in range(len(todo[i].getEstados())): #no terminal primero primero[0]  
                        if primero[0]==todo[i].getEstados()[first].getNombreEstado():
                            band1+=1
                            inicial = todo[i].getEstados()[first].getNombreEstado()
                            if todo[i].getEstados()[first].getEstadoSiguiente():
                                for k in range(len(todo[i].getEstados()[first].getEstadoSiguiente())):
                                    if varios[0] == todo[i].getEstados()[first].getEstadoSiguiente()[k]:
                                        ban4+=1
                                if ban4==0:
                                    todo[i].getEstados()[first].getEstadoSiguiente().append(varios[0])
                            else:
                                todo[i].getEstados()[first].getEstadoSiguiente().append(varios[0])
                    for fin in range(len(todo[i].getEstados())): #no terminial final varios[1] 
                        if varios[1]==todo[i].getEstados()[fin].getNombreEstado():
                            ban2+=1
                            final=todo[i].getEstados()[fin].getNombreEstado()
                    if ban1!=0 and ban2!=0 and ban3!=0:
                        if ban4==0:
                            si= Transiciones(inicial, final,varios[0])
                            todo[i].getTransicicones().append(si)
                        else:
                            input("Error, esta ingresando una transicion que ya existe: ")
                    else:
                        input("Error, un estado o un terminal que ingresa no existe: ") 
        else:
            ingresartransiciones=False


def CargarArchivoAFD():
    NArchivo= str(input("Ingrese el nombre del archivo de entrada: "))
    abrir_leer = open(NArchivo,'r')
    lee = abrir_leer.read()
    #abrir_leer.close()
    fragmentando = lee.split('%')
    try:
        fragmentando.remove('')
    except:
        pass
    for recorrer in range(len(fragmentando)):
        AFD=fragmentando[recorrer].split('\n')
        try:
            AFD.remove('')
            AFD.remove('')
        except:
            pass
        estado.append(AFD)
    for crea in range(len(estado)):
        ban=0
        for verificar in range(len(todo)):
            todo[verificar].getNombreAFD



def EvaluarCadena():
    print("Listar")
    """for LisAFD in automata:
        #AgrePre=""
        if LisAFD.getNombreAFD != "":
            if LisAFD.getNombreAFD(): #ver
                for Obtener in LisAFD.getNombreAFD():
                    #AgrePre=AgrePre+(LisCurso.getPrerrequisitos()[range])
                    #AgrePre+str(Obtener)
                    AgregarAFD=AgregarAFD+str(Obtener)
                    AgregarAFD=AgregarAFD +";"
                    #print(LisCurso.getPrerrequisitos()[range])
            AgregarAFD=AgregarAFD[:-1]
            print("[",LisAFD.getNombreAFD,",",LisAFD.getEstados(),",",AgrePre,",",LisCurso.getOpcionalidad()
            ,",",LisCurso.getSemestre(),",",LisCurso.getCreditos(),",",LisCurso.getEstado(), "]")
            print("[",LisAFD.getNombreAFD(),",",LisAFD.getEstados(),",",LisAFD.getAlfabeto(),",",LisAFD.getEstadoInicial(),",",LisAFD.getEstadosAceptacion(),",",LisAFD.getTransicicones(), "]")
        else:
            #agrepre-=1
            print("No hay AFD en el sistema")
        print("-------------------------")
    input("Presione enter para regresar al menu anterior: ")"""

