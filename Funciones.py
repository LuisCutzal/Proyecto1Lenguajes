import Automatas
import time
import os
import sys
import csv
global automata
automata=list()
global aceptacion
aceptacion=list()
global transi
transi = list()
def Agregar():
    #input("hola")
    #automata= Automatas.Automatas()
    nom=input("Ingrese el Nombre del AFD: ")
    #estados=input("Ingrese Estados del AFD separados por comas : ").split(',')
    ingreso=True
    while ingreso:
        estados=input("Ingrese Estados del AFD : ")
        aceptacion.append(list(estados))
        si=input("¿desea ingresar otro estado?, [Y/N]: ")
        if si=="Y" or si=="y" or si=="Yes":
            ingreso=True
        else:
            ingreso=False
    Alfabeto=input("Ingrese el Alfabeto del AFD separados por comas: ").split(',')
    EstadoInicial=input("Ingrese el Estado Inicial del AFD: ")
    EstadosAceptacion=input("Ingrese los Estados de Aceptacion del AFD separados por comas: ").split(',') #devuelve una lista
    otro=True
    while otro:
        Transicion = input("Ingrese las Transiciones del AFD: ").split('; |, ')
        transi.append(Transicion)
        si=input("¿desea ingresar otra transicion?, [Y/N]: ")
        if si=="Y" or si=="y" or si=="Yes":
            otro=True
        else:
            otro=False
    #automata.append(Automatas.Automatas(nom,estados,Alfabeto,EstadoInicial,EstadosAceptacion,Transicion))
    automata.append(Automatas.Automatas(nom,aceptacion,Alfabeto,EstadoInicial,EstadosAceptacion,transi))
    i=0
    j=0
    while i<len(aceptacion) and j<len(transi):
        print("[", nom , "," , aceptacion[i] , ",", Alfabeto , ",", EstadoInicial , ",", EstadosAceptacion , ",", transi[j] , "]")
        i+=1
        j+=1
    #print(aceptacion)
    input("Automata agregado correctamente, precione Enter para regresar: ")

def cargar():
    NArchivo= str(input("Ingrese el nombre del archivo de entrada: "))
    archivo=open(NArchivo)
    #leer = csv.reader(archivo)
    leer= archivo.readlines()
    #contador=0
    for tupla in leer:
        #if tupla =="%":
        #automata.append(Automatas.Automatas(tupla[0], tupla[1].split(','), tupla[2].split(','), tupla[3], tupla[4].split(','), tupla[5].split('; |, ')))
        automata.append(Automatas.Automatas(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5]))
        print(automata)
        input("hola")
    archivo.close()
    input("Archivo cargado correctamente, Presione enter para regresar: ")

def EvaluarCadena():
    print("Listar")
    for LisAFD in automata:
        #AgrePre=""
        if LisAFD.getNombreAFD != "":
            """if LisAFD.getNombreAFD(): #ver
                for Obtener in LisAFD.getNombreAFD():
                    #AgrePre=AgrePre+(LisCurso.getPrerrequisitos()[range])
                    #AgrePre+str(Obtener)
                    AgregarAFD=AgregarAFD+str(Obtener)
                    AgregarAFD=AgregarAFD +";"
                    #print(LisCurso.getPrerrequisitos()[range])
            AgregarAFD=AgregarAFD[:-1]
            print("[",LisAFD.getNombreAFD,",",LisAFD.getEstados(),",",AgrePre,",",LisCurso.getOpcionalidad()
            ,",",LisCurso.getSemestre(),",",LisCurso.getCreditos(),",",LisCurso.getEstado(), "]")"""
            print("[",LisAFD.getNombreAFD(),",",LisAFD.getEstados(),",",LisAFD.getAlfabeto(),",",LisAFD.getEstadoInicial(),",",LisAFD.getEstadosAceptacion(),",",LisAFD.getTransicicones(), "]")
        else:
            #agrepre-=1
            print("No hay AFD en el sistema")
        print("-------------------------")
    input("Presione enter para regresar al menu anterior: ")

