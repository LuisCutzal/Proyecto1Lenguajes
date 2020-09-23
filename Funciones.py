from Automatas import *
from Gramaticas import *
import time
import os
import sys
#from io import open 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#import subprocess
global ParteAutomata
ParteAutomata=list()
#ParteAutomata.append(Automatas)
global ParteGramatica
ParteGramatica=list()
#global Est
#Est=list()
#-----------comienza agregar respecto a automatas----------------
def AgregarAFD(): #agregar automatas manualmente
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
        #input("aceptar")
        #finaliza lo del nombre
        #--------------------------comienza Estados del AFD
        ingresoestados=True
        while ingresoestados:
            Ingrese_Estado=input("Ingrese Estado del AFD: ")
            tecleoEstado=Ingrese_Estado.upper()
            #for agrega in (range(len(ParteAutomata))):
                #ParteAutomata[agrega].getEstados().append(tecleoEstado)
            #Est.append(Estados(tecleoEstado))
            #creacionEstado = Est #verificar
            creacionEstado= Estados(tecleoEstado)
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
                            if comienza==0:
                                ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                                
                                #tengo que retornar
                            else:
                                input("El estado ya existe, no puede haber dos estados con el mismo  nombre: ")
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
                            if comienza==0:
                                ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                                
                                #tengo que retornar
                            else:
                                input("El estado ya existe, no puede haber dos estados con el mismo  nombre: ")
                                
                        else:
                            ParteAutomata[buscoEstado].getEstados().append(creacionEstado)
                ingresoestados=False
        #------------------------------termina EStados del AFD
        #------------------------------comienza Alfabeto del AFD
        ingresoAlfabeto=True
        while ingresoAlfabeto:
            Ingrese_alfabeto=str(input("Ingrese el Alfabeto del AFD: "))
            tecleoAlfabeto=Ingrese_alfabeto.lower()
            print("El caracter es: " +tecleoAlfabeto)
            condicionAlfa=input("¿Desea agregar otro Caracter?, escriba [Y/N]:")
            if condicionAlfa=="Y":
                for buscoAlfabeto in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[buscoAlfabeto].getNombreAFD():
                        if ParteAutomata[buscoAlfabeto].getNombreAFD():
                            comienzaA=0
                            for profundo2 in range(len(ParteAutomata[buscoAlfabeto].getAlfabeto())):
                                if tecleoAlfabeto == ParteAutomata[buscoAlfabeto].getAlfabeto()[profundo2]:
                                    comienzaA+=1
                            if comienzaA!=0:
                                input("El caracter ingresado ya existe, no se puede agregar: ")
                                #tengo que retornar
                            else:
                                ParteAutomata[buscoAlfabeto].getAlfabeto().append(tecleoAlfabeto)
                        else:
                            ParteAutomata[buscoAlfabeto].getAlfabeto().append(tecleoAlfabeto)
            else:
                for buscoAlfabeto in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[buscoAlfabeto].getNombreAFD():
                        if ParteAutomata[buscoAlfabeto].getNombreAFD():
                            comienzaA=0
                            for profundo2 in range(len(ParteAutomata[buscoAlfabeto].getAlfabeto())):
                                if tecleoAlfabeto == ParteAutomata[buscoAlfabeto].getAlfabeto()[profundo2]:
                                    comienzaA+=1
                            if comienzaA!=0:
                                input("El caracter ingresado ya existe, no se puede agregar: ")
                            else:
                                ParteAutomata[buscoAlfabeto].getAlfabeto().append(tecleoAlfabeto)
                        else:
                            ParteAutomata[buscoAlfabeto].getAlfabeto().append(tecleoAlfabeto)
                ingresoAlfabeto=False
        #------------------------------termina Alfabeto del AFD
        #-------------------------comienza estado inicial
        Einicial=str(input("Ingrese el Estado Inicial del AFD: "))
        Iguales=Einicial.upper()
        for buscoInicio in range(len(ParteAutomata)):
            if NombreAFD == ParteAutomata[buscoInicio].getNombreAFD():
                #input("aqui1")
                if ParteAutomata[buscoInicio].getEstados():
                    #input("aqui2")
                    for ahora in range(len(ParteAutomata[buscoInicio].getEstados())):
                        #input("aqui3")
                        if ParteAutomata[buscoInicio].getEstados()[ahora].getNombreEstado() == Iguales:
                            #input("aqui4")
                            for setear in range(len(ParteAutomata[buscoInicio].getEstados())):
                                ParteAutomata[buscoInicio].getEstados()[setear].setEstadoInicio(False)
                                """print("estado inicial es: " + Einicial)
                                input("primero")"""
                            ParteAutomata[buscoInicio].getEstados()[ahora].setEstadoInicio(True)
                            #print("estado es: " + Iguales)
                            #input("segundo")
                        #else:
                            #input("Ingreso un Estado que no Existe: ")
                            #tengo que retornar 
                else:
                    input("El AFD no cuenta con un estado para volverlo estado inicial: ")
        #-------------------------termina estado inicial
        #-------------------------comienza estados de aceptacion---------------------
        ingreseEstadoAceptacion=True
        while ingreseEstadoAceptacion:
            Ingerse_estadosAceptacion=str(input("Ingrese Estado de Aceptacion: "))
            tecleo_ingresoAceptacion=Ingerse_estadosAceptacion.upper()
            condicionA=input("¿Desea agregar otro Estado de Aceptacion?, escriba [Y/N]:")
            if condicionA=="Y":
                for buscoEstado in range(len(ParteAutomata)):
                    if NombreAFD==ParteAutomata[buscoEstado].getNombreAFD():
                        if ParteAutomata[buscoEstado].getEstados():
                            for busco in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if ParteAutomata[buscoEstado].getEstados()[busco].getNombreEstado()==tecleo_ingresoAceptacion:
                                    ParteAutomata[buscoEstado].getEstados()[busco].setEstadoAceptacion(True)
                                    print("el estado de aceptacion es: " + tecleo_ingresoAceptacion)
                                    #input("si")
                                #else:
                                    #input("Ingreso un estado que no existe: ")
                                    #tengo que retornar el ciclo while
                        else:
                            input("El AFD no cuenta con ningun Estado: ")
            else:
                for buscoEstado in range(len(ParteAutomata)):
                    if NombreAFD==ParteAutomata[buscoEstado].getNombreAFD():
                        if ParteAutomata[buscoEstado].getEstados():
                            for busco in range(len(ParteAutomata[buscoEstado].getEstados())):
                                if ParteAutomata[buscoEstado].getEstados()[busco].getNombreEstado()==tecleo_ingresoAceptacion:
                                    ParteAutomata[buscoEstado].getEstados()[busco].setEstadoAceptacion(True)
                                    print("el estado de aceptacion es: " + tecleo_ingresoAceptacion)
                                    #input("si")
                                else:
                                    input("Ingreso un estado que no existe: ")
                                    #tengo que retornar el ciclo while
                        else:
                            input("El AFD no cuenta con ningun Estado: ")
                ingreseEstadoAceptacion=False
        #-------------------------termina estados de aceptacion----------------------
        #-------------------------comienza las transiciones--------------------------
        Tra=True
        while Tra:
            Ingrese_transiciones=input("Ingrese Transiciones de la forma: A,0;B: ")
            input("Donde A es el Estado Inicial, 0 es parte del Alfabeto y B es el Estado Final")

            condiTra=input("¿Desea agregar otra Transicion?, escriba [Y/N]:")
            if condiTra=="Y":
                primero=Ingrese_transiciones.split(',')
                segundo=primero[1].split(';')
                SiPrimero=primero[0].upper()
                Sisegundo=segundo[1].upper()
                siAlfabeto=str(segundo[0].lower())
                for listo in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[listo].getNombreAFD():
                        alfa=0 #para el alfabeto
                        beta=0 #para el primer No terminal (osea estado)
                        sigma=0 #para el segundo No terminal (osea estado2)
                        gama=0 #contador
                        alcanzo = None
                        finalizo = None
                        #------------------comienza busqueda del alfabeto------------
                        for termi in range(len(ParteAutomata[listo].getAlfabeto())):
                            if siAlfabeto==ParteAutomata[listo].getAlfabeto()[termi]:
                                alfa+=1
                        #------------------termino busqueda del alfabeto--------
                        #------------------comienza busqueda del primer No terminal-------------
                        for first in range(len(ParteAutomata[listo].getEstados())):
                            if SiPrimero == ParteAutomata[listo].getEstados()[first].getNombreEstado():
                                beta+=1
                                alcanzo = ParteAutomata[listo].getEstados()[first]
                                if ParteAutomata[listo].getEstados()[first].getEstadoSiguiente():
                                    for buscando1 in range(len(ParteAutomata[listo].getEstados()[first].getEstadoSiguiente())):
                                        if siAlfabeto==ParteAutomata[listo].getEstados()[first].getEstadoSiguiente()[buscando1]:
                                            gama+=1
                                    if gama==0:
                                        ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append(siAlfabeto)
                                else:
                                    ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append(siAlfabeto)
                        #------------------termina busqueda del primer No terminal---------------
                        
                        #------------------comineza busqueda del segundo No terminal------------
                        for last in range(len(ParteAutomata[listo].getEstados())):
                            if Sisegundo == ParteAutomata[listo].getEstados()[last].getNombreEstado():
                                sigma+=1
                                finalizo = ParteAutomata[listo].getEstados()[last]
                        if alfa!=0 and beta !=0 and sigma!=0:
                            if gama==0:
                                si = Transiciones(alcanzo, finalizo, siAlfabeto)
                                ParteAutomata[listo].getTransicicones().append(si)
                            else:
                                input("Error, esta ingresando una transicion que ya existe: ")
                        else:
                            input("Error, un estado o un terminal que ingresa no existe: ") 
            else:
                primero=Ingrese_transiciones.split(',')
                segundo=primero[1].split(';')
                SiPrimero=primero[0].upper()
                Sisegundo=segundo[1].upper()
                siAlfabeto=str(segundo[0].lower())
                for listo in range(len(ParteAutomata)):
                    if NombreAFD == ParteAutomata[listo].getNombreAFD():
                        alfa=0 #para el alfabeto
                        beta=0 #para el primer No terminal (osea estado)
                        sigma=0 #para el segundo No terminal (osea estado2)
                        gama=0 #contador
                        alcanzo=None
                        finalizo=None
                        #------------------comienza busqueda del alfabeto-------------
                        for termi in range(len(ParteAutomata[listo].getAlfabeto())):
                            if siAlfabeto==ParteAutomata[listo].getAlfabeto()[termi]:
                                alfa+=1
                        #------------------termino busqueda del alfabeto--------
                        #------------------comienza busqueda del primer No terminal-------------
                        for first in range(len(ParteAutomata[listo].getEstados())):
                            if SiPrimero == ParteAutomata[listo].getEstados()[first].getNombreEstado():
                                beta+=1
                                alcanzo = ParteAutomata[listo].getEstados()[first]
                                if ParteAutomata[listo].getEstados()[first].getEstadoSiguiente():
                                    for buscando1 in range(len(ParteAutomata[listo].getEstados()[first].getEstadoSiguiente())):
                                        if SiPrimero==ParteAutomata[listo].getEstados()[first].getEstadoSiguiente()[buscando1]:
                                            gama+=1
                                    if gama==0:
                                        ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append(SiPrimero)
                                else:
                                    ParteAutomata[listo].getEstados()[first].getEstadoSiguiente().append(SiPrimero)
                        #------------------termina busqueda del primer No terminal---------------
                        
                        #------------------comineza busqueda del segundo No terminal------------
                        for last in range(len(ParteAutomata[listo].getEstados())):
                            if Sisegundo == ParteAutomata[listo].getEstados()[last].getNombreEstado():
                                sigma+=1
                                finalizo = ParteAutomata[listo].getEstados()[last]
                        if alfa==0 and beta==0 and sigma==0:
                            """if gama==0:
                                si = Transiciones(alcanzo, finalizo, siAlfabeto)
                                ParteAutomata[listo].getTransicicones().append(si)
                            else:
                                input("Error, esta ingresando una transicion que ya existe: ")"""
                            input("Error, un estado o un terminal que ingresa no existe: ")
                        else:
                            #input("Error, un estado o un terminal que ingresa no existe: ")
                            if gama==0:
                                si = Transiciones(alcanzo, finalizo, siAlfabeto)
                                ParteAutomata[listo].getTransicicones().append(si)
                            else:
                                input("Error, esta ingresando una transicion que ya existe: ")
                Tra=False
        #-------------------------termina las transiciones---------------------------
#-----------finaliza agregar respecto a automatas----------------

#------------comienza evaluar cadena del automata-------------------
def EvaluarCadena():
    input("Evaluar")
#------------finaliza evaluar cadena del automata


#************comienza agregar respecto a Gramaticas**************
def AgregarGramatica():
    NombreG=str(input("Ingrese el Nombre de la Gramatica: "))
    contadorNombreG=0
    for buscaNombreG in range(len(ParteGramatica)):
        if NombreG == ParteGramatica[buscaNombreG].getNombreGramatica():
            contadorNombreG+=1
    if contadorNombreG!=0:
        input("Ya existe un AFD con el mismo nombre, precione enter para regresar al menu anterior:")
    else:
        ParteGramatica.append(Gramaticas(NombreG))
        print("El nombre de la Gramatica es: "+ NombreG)
        #***********************comienza crear Terminales para la gramatica (alfabeto)***************
        Terminal=True
        while Terminal:
            ingreseTerminal=str(input("Ingrese un Terminal: "))
            TIngresado=ingreseTerminal.lower()
            print("El Terminal es: " + TIngresado)
            condicion0=input("¿Desea agregar otro Terminal?, escriba [Y/N]: ")
            if condicion0=="Y":
                for busca0 in range(len(ParteGramatica)):
                    if NombreG==ParteGramatica[busca0].getNombreGramatica():
                        if ParteGramatica[busca0].getNombreGramatica():
                            cominezaT=0
                            for capa1 in range(len(ParteGramatica[busca0].getAlfabeto())): #alfabeto=terminales
                                if TIngresado == ParteGramatica[busca0].getAlfabeto()[capa1]:
                                    cominezaT+=1
                            if cominezaT==0:
                                ParteGramatica[busca0].getAlfabeto().append(TIngresado)
                                
                                #*****************tengo que retornar para pedir que ingrese un terminal**************
                            else:
                                input("El Terminal ingresado ya existe, no se puede agregar: ")
                        else:
                            ParteGramatica[busca0].getAlfabeto().append(TIngresado)
            else:
                for busca0 in range(len(ParteGramatica)):
                    if NombreG==ParteGramatica[busca0].getNombreGramatica():
                        if ParteGramatica[busca0].getNombreGramatica():
                            cominezaT=0
                            for capa1 in range(len(ParteGramatica[busca0].getAlfabeto())): #alfabeto=terminales
                                if TIngresado == ParteGramatica[busca0].getAlfabeto()[capa1]:
                                    cominezaT+=1
                            if cominezaT==0:
                                ParteGramatica[busca0].getAlfabeto().append(TIngresado)
                                
                                #*****************tengo que retornar para pedir que ingrese un terminal**************
                            else:
                                input("El Terminal ingresado ya existe, no se puede agregar: ")
                                
                        else:
                            ParteGramatica[busca0].getAlfabeto().append(TIngresado)
                Terminal=False
        #***********************termina crear Terminal para gramatica (alfabeto)***************************
        #***********************comienza crear No terminales para la gramatica (estado)*************
        NoTerminal=True
        while NoTerminal:
            ingreseNoTerminal=str(input("Ingrese un No Terminal: "))
            NoIngresado=ingreseNoTerminal.upper()
            guardar=NoTerminales(NoIngresado)
            print("El No Terminal es: " + NoIngresado)
            condicion1=input("¿Desea agregar otro No Terminal?, escriba [Y/N]: ")
            if condicion1=="Y":
                for busca in range(len(ParteGramatica)):
                    if NombreG == ParteGramatica[busca].getNombreGramatica():
                        if ParteGramatica[busca].getNoTerminales():
                            com=0
                            for profundo in range(len(ParteGramatica[busca].getNoTerminales())):
                                if NoIngresado == ParteGramatica[busca].getNoTerminales()[profundo].getNombreNoTerminal():
                                    com+=1
                            if com==0:
                                ParteGramatica[busca].getNoTerminales().append(guardar)
                                
                            else:
                                input("El No Terminal ya existe, no puede haber dos No Terminales con el mismo  nombre: ")
                                
                        else:
                            ParteGramatica[busca].getNoTerminales().append(guardar)
            else:
                for busca in range(len(ParteGramatica)):
                    if NombreG == ParteGramatica[busca].getNombreGramatica():
                        if ParteGramatica[busca].getNoTerminales():
                            com=0
                            for profundo in range(len(ParteGramatica[busca].getNoTerminales())):
                                if NoIngresado == ParteGramatica[busca].getNoTerminales()[profundo].getNombreNoTerminal():
                                    com+=1
                            if com==0:
                                ParteGramatica[busca].getNoTerminales().append(guardar)
                            else:
                                input("El No Terminal ya existe, no puede haber dos No Terminales con el mismo  nombre: ")
                        else:
                            ParteGramatica[busca].getNoTerminales().append(guardar)
                NoTerminal=False
        #**********************finaliza crear No Terminales para la gramatica********************
        #**********************comienza asignar No Terminal inicial******************************
        NoTerminalInicial=str(input("Ingrese No Terminal Inicial de la Gramatica: "))
        Iguales1=NoTerminalInicial.upper()
        for vamos in range(len(ParteGramatica)):
            if NombreG == ParteGramatica[vamos].getNombreGramatica():
                #input("1")
                if ParteGramatica[vamos].getNoTerminales():
                    #input("2")
                    for buscoN in range(len(ParteGramatica[vamos].getNoTerminales())):
                        #input("3")
                        if ParteGramatica[vamos].getNoTerminales()[buscoN].getNombreNoTerminal() == Iguales1:
                            for cambia in range(len(ParteGramatica[vamos].getNoTerminales())):
                                #input("4")
                                ParteGramatica[vamos].getNoTerminales()[cambia].setEstadoInicial(False)
                            ParteGramatica[vamos].getNoTerminales()[buscoN].setEstadoInicial(True)
                            print("El No Terminal Incial es: " + Iguales1)
                            input("por fin")
                        else:
                            input("Ingreso un No Terminal que no Existe: ")
                            #tengo q retornar
                else:
                    input("La Gramatica no cuenta con un No Terminal para volverlo No Terminal inicial: ")
        #**********************finaliza asignar No Terminal inicial******************************
        #**********************comienza las producciones de la gramatica*************************
        Pro=True
        while Pro:
            ingreseProduccion=input("Ingrese Produccion de la gramatica, de la forma A>0 B: ")
            input("Donde A es el No Terminal Inicial, 0 es parte de los Terminales y B es el No Terminal Final")
            condiProducciones=input("¿Desea agregar otra Produccion?, escriba [Y/N]: ")
            if condiProducciones=="Y":
                P_primero=ingreseProduccion.split('>')
                P_segundo=P_primero[1].split(' ')
                PrimerNoTerminal=P_primero[0].upper()
                SegundoNoTerminal=P_segundo[1].upper()
                SiTerminal=str(P_segundo[0].lower())
                for inicio in range(len(ParteGramatica)):
                    if NombreG==ParteGramatica[inicio].getNombreGramatica():
                        alfaG=0
                        betaG=0
                        sigmaG=0
                        gamaG=0
                        alcanzoG=None
                        finalizoG=None
                        #******************comienza busqueda del primer No Terminal***********
                        for firstG in range(len(ParteGramatica[inicio].getNoTerminales())):
                            if PrimerNoTerminal==ParteGramatica[inicio].getNoTerminales()[firstG].getNombreNoTermina():
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
                        #******************termina busqueda del primer No Terminal***************
                        #******************comienza busqueda del Terminal************************
                        for TerminalG in range(len(ParteGramatica[inicio].getAlfabeto())):
                            if SiTerminal == ParteGramatica[inicio].getAlfabeto()[TerminalG]:
                                alfaG+=1
                        #******************termina busqueda del Terminal************************
                        #*******************comienza busqueda del segundo No Terminal***********
                        for second in range(len(ParteGramatica[inicio].getNoTerminales())):
                            if SegundoNoTerminal==ParteGramatica[inicio].getNoTerminales()[second].getNombreNoTermina():
                                sigmaG+=1
                                finalizoG=ParteGramatica[inicio].getNoTerminales()[second]
                        #******************finaliza busqueda del segundo No Terminal************
                        if alfaG==0 and betaG==0 and sigmaG==0:
                            """if gamaG==0:
                                siG=Producciones(alcanzoG,SiTerminal,finalizoG)
                                ParteGramatica[inicio].getProduccionesG().append(siG)
                            else:
                                input("Error, esta ingresando una produccion que ya existe: ")"""
                            input("Error, un No Terminal o un Terminal que ingresa no existe: ")
                        else:
                            #input("Error, un No Terminal o un Terminal que ingresa no existe: ")
                            if gamaG==0:
                                siG=Producciones(alcanzoG,SiTerminal,finalizoG)
                                ParteGramatica[inicio].getProduccionesG().append(siG)
                            else:
                                input("Error, esta ingresando una produccion que ya existe: ")
            else:
                P_primero=ingreseProduccion.split('>')
                P_segundo=P_primero[1].split(' ')
                PrimerNoTerminal=P_primero[0].upper()
                SegundoNoTerminal=P_segundo[1].upper()
                SiTerminal=str(P_segundo[0].lower())
                for inicio in range(len(ParteGramatica)):
                    if NombreG==ParteGramatica[inicio].getNombreGramatica():
                        alfaG=0
                        betaG=0
                        sigmaG=0
                        gamaG=0
                        alcanzoG=None
                        finalizoG=None
                        #******************comienza busqueda del primer No Terminal***********
                        for firstG in range(len(ParteGramatica[inicio].getNoTerminales())):
                            if PrimerNoTerminal==ParteGramatica[inicio].getNoTerminales()[firstG]:
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
                        #******************termina busqueda del primer No Terminal***************
                        #******************comienza busqueda del Terminal************************
                        for TerminalG in range(len(ParteGramatica[inicio].getAlfabeto())):
                            if SiTerminal == ParteGramatica[inicio].getAlfabeto()[TerminalG]:
                                alfaG+=1
                        #******************termina busqueda del Terminal************************
                        #*******************comienza busqueda del segundo No Terminal***********
                        for second in range(len(ParteGramatica[inicio].getNoTerminales())):
                            if SegundoNoTerminal==ParteGramatica[inicio].getNoTerminales()[second]:
                                sigmaG+=1
                                finalizoG=ParteGramatica[inicio].getNoTerminales()[second]
                        if alfaG==0 and betaG==0 and sigmaG==0:
                            """if gamaG==0:
                                siG=Producciones(alcanzoG,SiTerminal,finalizoG)
                                ParteGramatica[inicio].getProduccionesG().append(siG)
                            else:
                                input("Error, esta ingresando una produccion que ya existe: ")"""
                            input("Error, un No Terminal o un Terminal que ingresa no existe: ")
                        else:
                            #input("Error, un No Terminal o un Terminal que ingresa no existe: ")
                            if gamaG==0:
                                siG=Producciones(alcanzoG,SiTerminal,finalizoG)
                                ParteGramatica[inicio].getProduccionesG().append(siG)
                            else:
                                input("Error, esta ingresando una produccion que ya existe: ")
                Pro=False
                
        #**********************finaliza las producciones de la gramatica*************************





#************finaliza agregar respecto a Gramaticas**************