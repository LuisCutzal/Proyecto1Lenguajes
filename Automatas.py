class Automatas (object):
    def __init__(self,nombre,estados,alfabeto,estado_inicial,estados_aceptacion,transiciones):
        self.nombre_afd=nombre #tipo string
        self.estados=estados #list() #tipo lista
        self.alfabeto=alfabeto #list() #tipo lista
        self.estado_inicial=estado_inicial #tipo string
        self.estados_aceptacion=estados_aceptacion #list() #tipo lista
        self.transiciones=transiciones #list() #tipo lista

#---------------get----------------
    def getNombreAFD(self):
        return str(self.nombre_afd)

    def getEstados(self):
        return list(self.estados)

    def getAlfabeto(self):
        return list(self.alfabeto)

    def getEstadoInicial(self):
        return str(self.estado_inicial)

    def getEstadosAceptacion(self):
        return list(self.estados_aceptacion)
    
    def getTransicicones(self):
        return list(self.transiciones)
    
#---------------get----------------
    def setNombreAFD(self, nuevoNombre):
        self.nombre_afd=str(nuevoNombre)
    
    def setEstados(self, nuevosEstados):
        self.estados = list(nuevosEstados)
    
    def setAlfabeto(self, nuevoAlfabeto):
        self.alfabeto = list(nuevoAlfabeto)
    
    def setEstadoInicial(self,nuevoEstadoInicial):
        self.estado_inicial = str(nuevoEstadoInicial)
    
    def setEstadosAceptacion(self, nuevoEstadosAceptacion ):
        self.estados_aceptacion = list(nuevoEstadosAceptacion)
    
    def setTransiciones(self, nuevasTransiciones):
        self.transiciones = list(nuevasTransiciones)

    def __str__(self):
        return (self.nombre_afd, self.estados, self.alfabeto, self.estado_inicial, self.estados_aceptacion, self.transiciones)