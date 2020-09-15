import Automatas
import time
import os
global automata
automata=list()
global aceptacion
aceptacion=list()

def Agregar():
    #input("hola")
    #automata= Automatas.Automatas()
    nom=input("Ingrese el Nombre del AFD: ")
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
    Transicion = input("Ingrese las Transiciones del AFD: ").split('; |, ')
    automata.append(Automatas.Automatas(nom,aceptacion,Alfabeto,EstadoInicial,EstadosAceptacion,Transicion))
    print("[", nom , "," , aceptacion , ",", Alfabeto , ",", EstadoInicial , ",", EstadosAceptacion , ",", Transicion , "]")
    input("hola: ")