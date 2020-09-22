class Gramaticas(object):
    def __init__(self,nombreG):
        self.NombreGramaticas=str(nombreG)
        self.Alfabeto=list() #Terminales
        self.NoTerminales=list() #simbolos
        self.Producciones=list()
        self.Inicio=None
        self.Izq=False
        self.NoPre=None
#--------------gets-------------------
    def getNombreGramatica(self):
        return str(self.NombreGramaticas)
    def getAlfabeto(self):
        return self.Alfabeto
    def getNoTerminales(self):
        return self.NoTerminales
    def getProduccionesG(self):
        return self.Producciones
    def getInicio(self):
        return self.Inicio
    def getIzq(self):
        return self.Izq
    def getNoPre(self):
        return self.NoPre
#-----------sets-------------------
    def setNombreGramatica(self,NuevoNombreG):
        self.NombreGramaticas=NuevoNombreG
    def setAlfabeto(self, NuevoAlfa):
        self.Alfabeto=NuevoAlfa
    def setNoTerminales(self,NuevoNoTerminal):
        self.NoTerminales=NuevoNoTerminal
    def setProducciones(self,NuevaProduccion):
        self.Producciones=NuevaProduccion
    def setInicio(self,NuevoInicio):
        self.Inicio=NuevoInicio
    def setIzq(self,NuevaIzquierda):
        self.Izq=NuevaIzquierda
    def setNoPre(self,NuevoNoPre):
        self.NoPre=NuevoNoPre

class NoTerminales(object):
    def __init__(self,NombreNoTerminal):
        self.NombreNoTerminales=NombreNoTerminal
        self.estadoInicial=False
        self.estadoSiguiente=list()
        self.aceptacion=False #es epsilon
#---------------gets----------------------
    def getNombreNoTerminal(self):
        return self.NombreNoTerminales
    def getEstadoInicial(self):
        return self.estadoInicial
    def getEstadoSiguiente(self):
        return self.estadoSiguiente
    def getAceptacion(self):
        return self.aceptacion
#------------------sets-----------------------
    def setNombreNoTerminal(self,NuevoNombreNoTerminal):
        self.NombreNoTerminales = NuevoNombreNoTerminal
    def setEstadoInicial(self,NuevoEstadoInicial):
        self.estadoInicial=NuevoEstadoInicial
    def setEstadoSiguiente(self, NuevoEstadoSiguiente):
        self.estadoSiguiente=NuevoEstadoSiguiente
    def setAceptacion(self,NuevaAceptacion):
        self.aceptacion=NuevaAceptacion

class Producciones(object):
    def __init__(self,NTerminalInicial,Alfa,NTerminalSiguiente):
        self.NTerminalInicial=NTerminalInicial
        self.Alfabeto=Alfa
        self.NTerminalSiguiente=NTerminalSiguiente
#----------------gets--------------------------
    def getTerminalInicial(self):
        return self.NTerminalInicial
    def getAlfabetoProducciones(self):
        return self.Alfabeto
    def getTerminalSiguiente(self):
        return self.NTerminalSiguiente
#------------sets-------------------------
    def setTerminalInicial(self,NuevoTerminalInicial):
        self.NTerminalInicial=NuevoTerminalInicial
    def setAlfabetoProducciones(self,NuevoAlfabetoProducciones):
        self.Alfabeto=NuevoAlfabetoProducciones
    def setTerminalSiguiente(self,NuevoTerminalSiguiente):
        self.NTerminalSiguiente=NuevoTerminalSiguiente

