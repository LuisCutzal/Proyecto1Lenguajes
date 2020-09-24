from Automatas import *
from Gramaticas import *
import time
import os
import sys
from io import open 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from Funciones import *

global automatacarga
automatacarga=list()
global gramaticacarga
gramaticacarga=list()
#inicia carga masiva para el AFD
def CargarArchivoAFD():
    #input("Cargar AFD")
    nombreArchivoAFD=input("Ingrese el nombre del Archivo para Cargar AFD´s: ")
    abrirAFD= open(nombreArchivoAFD, 'r')
    leer = abrirAFD.read()
    abrirAFD.close()
    tuplasAFD=leer.split('%')
    try:
        tuplasAFD.remove('')
    except:
        pass
    for comienza in range(len(tuplasAFD)):
        auto=tuplasAFD[comienza].split('\n')
        try:
            auto.remove('')
            auto.remove('')
        except:
            pass
        automatacarga.append(auto)
    #comienzo a crear y agregar datos
    for agre in range(len(automatacarga)):
        head=0
        for buscoNombre in range(len(ParteAutomata)):
            if automatacarga[agre][0] == ParteAutomata[buscoNombre].getNombreAFD():
                #input("si")
                head+=1
        if head==0:
            #input("si: ")
            Nombre = str(automatacarga[agre][0])
            nombreAFD = Automatas(Nombre)
            ParteAutomata.append(nombreAFD)
            print("el nombre es: " + Nombre)
            input("si:")
            #estados
            estadoleido=automatacarga[agre][1].split(',') #es como haber introducido un automata manualmente
            #print("estados" + str(estadoleido))
            #input("verifico como viene el estado leido:")
            for forma in range(len(estadoleido)):
                creacionEstado= Estados(estadoleido[forma])
                for buscoEstado in range(len(ParteAutomata)):
                    if Nombre == ParteAutomata[buscoEstado].getNombreAFD():
                        if ParteAutomata[buscoEstado].getEstados():
                            comienza=0
                            for profundo in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if estadoleido[forma] == ParteAutomata[buscoEstado].getEstados()[profundo].getNombreEstado():
                                    comienza+=1
                            if comienza==0:
                                ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                                #input("Los estados son:" + str(estadoleido))
                                #input("si, estados")
                            else:
                                input("El estado ya existe, no puede haber dos estados con el mismo  nombre: ")
                        else:
                            ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
            input("Los estados son:" + str(estadoleido))
            #alfabeto
            alfabetoleido=automatacarga[agre][2].split(',')
            for cuerpo in range(len(alfabetoleido)):
                for buscoAlfabeto in range(len(ParteAutomata)):
                    if str(automatacarga[agre][0]) == ParteAutomata[buscoAlfabeto].getNombreAFD():
                        if ParteAutomata[buscoAlfabeto].getNombreAFD():
                            comienzaA=0
                            for profundo2 in range(len(ParteAutomata[buscoAlfabeto].getAlfabeto())):
                                if str(alfabetoleido[cuerpo]) == ParteAutomata[buscoAlfabeto].getAlfabeto()[profundo2]:
                                    comienzaA+=1
                                if comienzaA==0:
                                    ParteAutomata[buscoAlfabeto].getAlfabeto().append(str(alfabetoleido))
                                    input("El alfabeto es: " + str(alfabetoleido))
                                else:
                                    input("El caracter ingresado ya existe, no se puede agregar: ")
                            else:
                                ParteAutomata[buscoAlfabeto].getAlfabeto().append(str(alfabetoleido))
            #estado inicial
            inicioleido= str(automatacarga[agre][3])
            for buscoInicio in range(len(ParteAutomata)):
                if str(automatacarga[agre][0]) == ParteAutomata[buscoInicio].getNombreAFD():
                    if ParteAutomata[buscoInicio].getEstados():
                        for ahora in range(len(ParteAutomata[buscoInicio].getEstados())):
                            if ParteAutomata[buscoInicio].getEstados()[ahora].getNombreEstado() == inicioleido:
                                for setear in range(len(ParteAutomata[buscoInicio].getEstados())):
                                    ParteAutomata[buscoInicio].getEstados()[setear].setEstadoInicio(False)
                                ParteAutomata[buscoInicio].getEstados()[ahora].setEstadoInicio(True)
                                input("el estado inicial es: "+ inicioleido)
                            """else:
                                input("Ingreso un Estado que no Existe, esto es de estado inicial: ")"""
                    else:
                        input("El AFD no cuenta con un estado para volverlo estado inicial: ")
            #estados de aceptacion
            try:
                aceptacionleido=automatacarga[agre][4].split(',')
                aceptacionleido.remove('')
            except:
                pass
            for ace in range(len(aceptacionleido)):
                for buscoEstado in range(len(ParteAutomata)):
                    if str(automatacarga[agre][0])==ParteAutomata[buscoEstado].getNombreAFD():
                        if ParteAutomata[buscoEstado].getEstados():
                            for busco in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if ParteAutomata[buscoEstado].getEstados()[busco].getNombreEstado()==aceptacionleido[ace]:
                                    ParteAutomata[buscoEstado].getEstados()[busco].setEstadoAceptacion(True)
                                    input("El estado de Aceptacion es: "+ aceptacionleido[ace])
                                #else:
                                    #input("Ingreso un estado que no existe, esto es de estado de aceptacion: ")
                        else:
                            input("El AFD no cuenta con ningun Estado: ")
            #transiciones
            for termino in range(len(automatacarga[agre])):
                if termino>=5:
                    primero=automatacarga[agre][termino].split(',')
                    segundo=primero[1].split(';')
                    SiPrimero=(primero[0].upper())
                    Sisegundo=(segundo[1].upper())
                    siAlfabeto=str(segundo[0].lower())
                    #input("Estado primero:"+ str(SiPrimero))
                    #input("Estado segundo:"+ str(Sisegundo))
                    #input("alfabeto:"+ str(siAlfabeto))
                    for listo in range(len(ParteAutomata)):
                        if str(automatacarga[agre][0]) == ParteAutomata[listo].getNombreAFD():
                            alfa=0
                            beta=0
                            sigma=0
                            gama=0
                            alcanzo=None
                            finalizo = None
                            #-----------------alfabeto--------------
                            for termi in range(len(ParteAutomata[listo].getAlfabeto())):
                                if siAlfabeto==ParteAutomata[listo].getAlfabeto()[termi]:
                                    alfa+=1
                            #----------------fin alfabeto-----------
                            for first in range(len(ParteAutomata[listo].getEstados())):
                                if SiPrimero == ParteAutomata[listo].getEstados()[first].getNombreEstado():
                                    beta+=1
                                    alcanzo = ParteAutomata[listo].getEstados()[first]
                                    if ParteAutomata[listo].getEstados()[first].getEstadoSiguiente():
                                        for buscando1 in range(len(ParteAutomata[listo].getEstados()[first].getEstadoSiguiente())):
                                            if siAlfabeto==ParteAutomata[listo].getEstados()[first].getEstadoSiguiente()[buscando1]:
                                                gama+=1
                                        if gama==0:
                                            ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append((siAlfabeto))
                                    else:
                                        ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append((siAlfabeto))
                            
                            for last in range(len(ParteAutomata[listo].getEstados())):
                                if (Sisegundo) == ParteAutomata[listo].getEstados()[last].getNombreEstado():
                                    sigma+=1
                                    finalizo = ParteAutomata[listo].getEstados()[last]

                            #---------------agregamos--------------
                            if alfa==0 and beta==0 and sigma==0:
                                """if gama==0:
                                    si = Transiciones((alcanzo), (finalizo), (siAlfabeto))
                                    ParteAutomata[listo].getTransicicones().append(si)
                                else:
                                    input("Error, esta ingresando una transicion que ya existe: ")"""
                                input("Error, un estado o un terminal que ingresa no existe: ")
                            else:
                                #input("Error, un estado o un terminal que ingresa no existe: ")
                                if gama==0:
                                    si = Transiciones((alcanzo),(siAlfabeto), (finalizo) )
                                    ParteAutomata[listo].getTransicicones().append(si)
                                else:
                                    input("Error, esta ingresando una transicion que ya existe: ")
            input("Archivo cargado: ")                              
#finaliza carga masiva para el AFD

#inicia carga masiva para la Gamatica
def CargarArchivoGramatica():
    #input("Cargar Gramatica")
    nombreArchivoGramatica=input("Ingrese el nombre del Archivo para Cargar las Gramaticas: ")
    abrirGramatica=open(nombreArchivoGramatica, 'r')
    leerG=abrirGramatica.read()
    abrirGramatica.close()
    tuplasGram=leerG.split('%')
    try:
        tuplasGram.remove('')
    except:
        pass
    for comienzaG in range(len(tuplasGram)):
        grama=tuplasGram[comienzaG].split('\n')
        try:
            grama.remove('')
            grama.remove('')
        except:
            pass
        gramaticacarga.append(grama)
    #comenzamos
    for agreG in range(len(gramaticacarga)):
        headg=0
        for buscoNombreG in range(len(ParteGramatica)):
            if str(gramaticacarga[agreG][0])==ParteGramatica[buscoNombreG].getNombreGramatica():
                headg+=1
        if headg==0:
            NombreG=str(gramaticacarga[agreG][0])
            nombreGram=Gramaticas(NombreG)
            ParteGramatica.append(nombreGram)
            input("El nombre de la Gramatica es: " + NombreG)
            #No Terminales
            NoTerminalleido=gramaticacarga[agreG][1].split(',')
            for formaG in range(len(NoTerminalleido)):
                creacionNo=NoTerminales(NoTerminalleido[formaG])
                for buscoNo in range(len(ParteGramatica)):
                    if NombreG == ParteGramatica[buscoNo].getNombreGramatica():
                        if ParteGramatica[buscoNo].getNoTerminales():
                            comienzaG=0
                            for profundoG in range(len(ParteGramatica[buscoNo].getNoTerminales())):
                                if (NoTerminalleido[formaG]) == ParteGramatica[buscoNo].getNoTerminales()[profundoG].getNombreNoTerminal():
                                    comienzaG+=1
                            if comienzaG==0:
                                ParteGramatica[buscoNo].getNoTerminales().append(creacionNo)
                            else:
                                input("El No Terminal ya existe: ")
                        else:
                            ParteGramatica[buscoNo].getNoTerminales().append(creacionNo)
            input("Los No Terminales son: " +str(NoTerminalleido))
            #alfabeto
            Terminalleido=gramaticacarga[agreG][2].split(',')
            for cuerpo in range(len(Terminalleido)):
                for busca0 in range(len(ParteGramatica)):
                    if NombreG==ParteGramatica[busca0].getNombreGramatica():
                        if ParteGramatica[busca0].getNombreGramatica():
                            cominezaT=0
                            for capa1 in range(len(ParteGramatica[busca0].getAlfabeto())):
                                if str(Terminalleido[cuerpo]) == ParteGramatica[busca0].getAlfabeto()[capa1]:
                                    cominezaT+=1
                            if cominezaT==0:
                                ParteGramatica[busca0].getAlfabeto().append(Terminalleido)
                            else:
                                input("El Terminal ingresado ya existe, no se puede agregar: ")
                        else:
                             ParteGramatica[busca0].getAlfabeto().append(Terminalleido)
            #terminal inicial
            NoTerminalInicial=str(gramaticacarga[agreG][3])
            for vamos in range(len(ParteGramatica)):
                if NombreG == ParteGramatica[vamos].getNombreGramatica():
                    if ParteGramatica[vamos].getNoTerminales():
                        for buscoN in range(len(ParteGramatica[vamos].getNoTerminales())):
                            if ParteGramatica[vamos].getNoTerminales()[buscoN].getNombreNoTerminal() == NoTerminalInicial:
                                for cambia in range(len(ParteGramatica[vamos].getNoTerminales())):
                                    ParteGramatica[vamos].getNoTerminales()[cambia].setEstadoInicial(False)
                                ParteGramatica[vamos].getNoTerminales()[buscoN].setEstadoInicial(True)
                                input("El No Terminal Incial es: " + str(NoTerminalInicial))
                            """else:
                                input("Ingreso un No Terminal que no Existe: ")"""
                    else:
                        input("La Gramatica no cuenta con un No Terminal para volverlo No Terminal inicial: ")
            #producciones
            for alfin in range(len(gramaticacarga[agreG])):
                if alfin>=4:
                    P_primero=gramaticacarga[agreG][alfin].split('>')
                    P_segundo=P_primero[1].split(' ')
                    if len(P_segundo)>1:
                        PrimerNoTerminal=P_primero[0].upper()
                        SegundoNoTerminal=P_segundo[1].upper()
                        SiTerminal=str(P_segundo[0].lower())
                        input("No Terminal Inicial: " + str(PrimerNoTerminal))
                        input("Terminal: " + str(SiTerminal))
                        input("No Terminal Siguiente: " + str(SegundoNoTerminal))
                        for inicio in range(len(ParteGramatica)):
                            if str(gramaticacarga[agreG][0])==ParteGramatica[inicio].getNombreGramatica():
                                alfaG=0
                                betaG=0
                                sigmaG=0
                                gamaG=0
                                alcanzoG= None
                                finalizoG= None
                                #-------------------------------alfabeto----------------------
                                for TerminalG in range(len(ParteGramatica[inicio].getAlfabeto())):
                                    if SiTerminal == ParteGramatica[inicio].getAlfabeto()[TerminalG]:
                                        alfaG+=1
                                #----------------------------fin alfabeto----------------------
                                for firstG in range(len(ParteGramatica[inicio].getNoTerminales())):
                                    if (PrimerNoTerminal)==ParteGramatica[inicio].getNoTerminales()[firstG].getNombreNoTerminal():
                                        betaG+=1
                                        alcanzoG = ParteGramatica[inicio].getNoTerminales()[firstG]
                                        if ParteGramatica[inicio].getNoTerminales()[firstG].getEstadoSiguiente():
                                            for buscando1G in range(len(ParteGramatica[inicio].getNoTerminales()[firstG].getEstadoSiguiente())):
                                                if SiTerminal==ParteGramatica[inicio].getNoTerminales()[firstG].getEstadoSiguiente()[buscando1G]:
                                                    gamaG+=1
                                            if gamaG==0:
                                                ParteGramatica[inicio].getNoTerminales()[firstG].getEstadoSiguiente().append(SiTerminal)
                                        else:
                                            ParteGramatica[inicio].getNoTerminales()[firstG].getEstadoSiguiente().append(SiTerminal)
                                for second in range(len(ParteGramatica[inicio].getNoTerminales())):
                                    if (SegundoNoTerminal)==ParteGramatica[inicio].getNoTerminales()[second].getNombreNoTerminal():
                                        sigmaG+=1
                                        finalizoG=ParteGramatica[inicio].getNoTerminales()[second]
                                #------------------agregamos-----------------
                                if alfaG==0 and betaG==0 and sigmaG==0:
                                    input("Error, un No Terminal o un Terminal que ingresa no existe: ")
                                else:
                                    if gamaG==0:
                                        siG=Producciones(alcanzoG,SiTerminal,finalizoG)
                                        ParteGramatica[inicio].getProduccionesG().append(siG)
                                    else:
                                        input("Error, Una produccion ya Existe: ")
                    else:
                        if P_segundo[0]=="$":
                            for acept in range(len(ParteGramatica)):
                                if NombreG==ParteGramatica[acept].getNombreGramatica():
                                    for yes in range(len(ParteGramatica[acept].getNoTerminales())):
                                        if P_primero[0]==ParteGramatica[acept].getNoTerminales()[yes].getNombreNoTerminal():
                                            ParteGramatica[acept].getNoTerminales()[yes].setAceptacion(True)
                        input("ingreso el caracter $")

    input("Archivo cargado: ") 
#finaliza carga masiva para la Gramatica