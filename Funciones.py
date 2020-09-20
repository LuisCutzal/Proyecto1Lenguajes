from Automatas import *
from Gramaticas import *
import time
import os
import sys
from io import open 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#import subprocess
global ParteAutomata
ParteAutomata=list()
#ParteAutomata.append(Automatas)
global ParteGramatica
ParteGramatica=list()

#-----------comienza todo respecto a automatas----------------
def Agregar(): #agregar automatas manualmente
    #Comienza lo del nombre
    NombreAFD=str(input("Ingrese el nombre del AFD: "))
    ContadorNombre=0
    for buscaNombre in range(len(ParteAutomata)):
        if NombreAFD==ParteAutomata[buscaNombre].getNombreAFD():
            ContadorNombre+=1 #busca si hay un nombre igual agregado en el objeto Automatas
    if ContadorNombre!=0:
        input("Ya existe un AFD con el mismo nombre, precione enter para regresar al menu anterior:")
    else:
        ParteAutomata.append(Automatas(NombreAFD))
        print("El nombre del AFD es: " + NombreAFD)
        input("aceptar")
        #finaliza lo del nombre
        #--------------------------comienza Estados del AFD
        ingresoestados=True
        while ingresoestados:
            Ingrese_Estado=input("Ingrese Estado del AFD: ")
            tecleoEstado=Ingrese_Estado.upper()
            #for agrega in (range(len(ParteAutomata))):
                #ParteAutomata[agrega].getEstados().append(tecleoEstado)
            creacionEstado = Estados(tecleoEstado) #verificar
            print("el Estado es: " + tecleoEstado)
            condicion=input("¿Desea agregar otro estado?, escriba [Y/N]: ")
            if condicion=="Y":
                for buscoEstado in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[buscoEstado].getNombreAFD(): #para hacer que solo busque en el automata con el nombre ingresado
                        if ParteAutomata[buscoEstado].getEstados():
                            comienza=0
                            for profundo in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if tecleoEstado == ParteAutomata[buscoEstado].getEstados()[profundo].getNombreEstado():
                                    comienza+=1
                            if comienza!=0:
                                input("El estado ya existe, no puede haber dos estados con el mismo  nombre: ")
                            else:
                                ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                        else:
                            ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
            else:
                #input("gracias")
                for buscoEstado in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[buscoEstado].getNombreAFD(): #para hacer que solo busque en el automata con el nombre ingresado
                        if ParteAutomata[buscoEstado].getEstados():
                            comienza=0
                            for profundo in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if tecleoEstado == ParteAutomata[buscoEstado].getEstados()[profundo].getNombreEstado():
                                    comienza+=1
                            if comienza!=0:
                                input("El estado ya existe, no puede haber dos estados con el mismo  nombre: ")
                            else:
                                ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                        else:
                            ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                ingresoestados=False
        #------------------------------termina EStados del AFD


#-----------finaliza todo respecto a automatas----------------

#----------comienza lo de cargar Archivo de Automatas---------------
def CargarArchivoAFD():
    input("cargar")
#----------finaliza lo de cargar Archivo de Automatas--------------

#------------comienza evaluar cadena del automata-------------------
def EvaluarCadena():
    input("Evaluar")
#------------finaliza evaluar cadena del automata