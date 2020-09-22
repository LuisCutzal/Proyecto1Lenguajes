class Automatas (object):
    def __init__(self, nombre): #veremos
        self.nombre_afd = str(nombre) #tipo string
        self.estados=list() #tipo lista
        self.alfabeto=list() #tipo lista
        self.estado_inicial=None #tipo string
        self.estados_aceptacion=list() #tipo lista
        self.transiciones=list() #tipo lista
#---------------get----------------
    def getNombreAFD(self):
        return str(self.nombre_afd)

    def getEstados(self):
        return (self.estados)

    def getAlfabeto(self):
        return (self.alfabeto)

    def getEstadoInicial(self):
        return (self.estado_inicial)

    def getEstadosAceptacion(self):
        return (self.estados_aceptacion)
    
    def getTransicicones(self):
        return (self.transiciones)
    
#---------------set----------------
    def setNombreAFD(self, nuevoNombre):
        self.nombre_afd=(nuevoNombre)
    
    def setEstados(self, nuevosEstados):
        self.estados = (nuevosEstados)
    
    def setAlfabeto(self, nuevoAlfabeto):
        self.alfabeto = (nuevoAlfabeto)
    
    def setEstadoInicial(self,nuevoEstadoInicial):
        self.estado_inicial = (nuevoEstadoInicial)
    
    def setEstadosAceptacion(self, nuevoEstadosAceptacion ):
        self.estados_aceptacion = (nuevoEstadosAceptacion)
    
    def setTransiciones(self, nuevasTransiciones):
        self.transiciones = (nuevasTransiciones)

    
class Estados(object):
    def __init__(self, nombre):
        self.nombre=nombre
        self.EstadoAceptacion=False #dato boolean
        self.Estadoinicio=False #dato boolean
        self.EstadoSiguiente=list()

#-----------------get-----------------------
    def getNombreEstado(self):
        return str(self.nombre)
    
    def getEstadoAceptacion(self):
        return self.EstadoAceptacion
    
    def getEstadoInicio(self):
        return self.Estadoinicio
    
    def getEstadoSiguiente(self):
        return self.EstadoSiguiente
#-------------------set---------------------
    def setEstadoAceptacion(self, NuevoEstadoAceptacion):
        self.EstadoAceptacion = NuevoEstadoAceptacion
    
    def setEstadoInicio(self, NuevoEstadoInicial):
        self.Estadoinicio = NuevoEstadoInicial
    
    def setEstadoFinal(self, NuevoEstadoSiguiente):
        self.EstadoSiguiente= NuevoEstadoSiguiente


class Transiciones(object): #para todas las transiciones de un afd
    def __init__(self, inicioTrans, finTrans, datoTrans):
        self.estadoInicial=inicioTrans
        self.estadoFinal=finTrans
        self.entradato=datoTrans
#---------------get--------------------
    def getEstadoInicialTransicion(self):
        return self.estadoInicial
    
    def getEstadoFinalTransicion(self):
        return self.estadoFinal
    
    def getDatoTransicion(self):
        return self.entradato

#--------------set-----------------------
    def setEstaodInicialTransicion(self, NuevoEstadoInicioTransicion):
        self.estadoInicial = (NuevoEstadoInicioTransicion)
    
    def setEstadoFinalTransicion(self, NuevoEstadoFinalTransicion):
        self.estadoFinal = NuevoEstadoFinalTransicion
    
    def setDatoTransicion(self,NuevoDatoTransicion):
        self.entradato = NuevoDatoTransicion
#---------------------todo esto es igual para la gramatica---------------------