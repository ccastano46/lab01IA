import math
class Estado:
    def __init__(self, nombre, heuristico):
        self.nombre = nombre
        self.heuristico = heuristico
        self.acciones = []
        self.sucesores = []

    def setAccion(self, sucesor, costo):
        self.acciones.append(Accion(self, sucesor, costo))
        self.sucesores.append(sucesor)

    def getAccion(self, sucesor):
        for accion in self.acciones:
            if (self == accion.getPadre() and sucesor == accion.getSucesor()): return accion

    def getNombre(self):
        return self.nombre

    def getHeuristico(self):
        return self.heuristico
    def __eq__(self, e):
        if (self.nombre == e.nombre and self.heuristico == e.heuristico):
            return True
        else:
            return False
    def getSucesores(self):
        return self.sucesores
    def __str__(self):
        return self.nombre


class Accion:
    def __init__(self, estado1, estado2, costo):
        self.estado1 = estado1
        self.estado2 = estado2
        self.costo = costo
    def getSucesor(self):
        return self.estado2

    def getPadre(self):
        return self.estado1
    def __str__(self):
        return [self.estado1.nombre, self.estado2.nombre, self.costo]


class EspacioDeEstados:
    def __init__(self,inicial,objetivo):
        self.inicial = inicial
        self.objetivo = objetivo
        self.estados = []
        self.estados.append(self.inicial)
        self.estados.append(self.objetivo)
    def setEstado(self,nombre,heuristico):
        self.estados.append(Estado(nombre,heuristico))

    def setAccion(self,e1,e2,costo):
        encontrado = False
        if (e1 in self.estados and e2 in self.estados):
                self.estados[self.estados.index(e1)].setAccion(self.estados[self.estados.index(e2)],costo)
        if not(e1 in self.estados): print(f"{e1} no es un estado valido")
        elif not(e2 in self.estados):print(f"{e2} no es un estado valido")
        else: print("Accion registrada")
    def initial(self):
        return self.inicial
    def actionResults(self, estado):
        return self.estados[self.estados.index(estado)].sucesores
    def isGoal(self,estado):
        return estado == self.objetivo

    def seleccionar_ganador(self,minimo,frontera,ganador):
        actual_ganador = ganador
        for llave in frontera:
            if (frontera[llave] < minimo):
                actual_ganador = llave
                minimo = frontera[llave]
        return actual_ganador, minimo
    def buscar_estado(self,nombre):
        estado = None
        for e in self.estados:
            if(nombre == e.nombre):
                estado= e
                break
        return estado

    def actionCost(self,inicial,objetivo):
        if(inicial== objetivo):
            return 0
        else:
            frontera = {(inicial.nombre): 0}
            ganador = (inicial.nombre)

            while not(objetivo.nombre in ganador):
                minimo = math.inf
                padre = self.buscar_estado(ganador[len(ganador) - 1])
                sucesores = padre.getSucesores()
                anterior = frontera[ganador]
                del frontera[ganador]
                prototipo = tuple(ganador)
                for s in sucesores:
                    frontera[prototipo + (s.nombre,)] = padre.getAccion(s).costo + anterior
                    ganador, minimo = self.seleccionar_ganador(minimo,frontera,ganador)
            return frontera[ganador]


    def heuristicCost(self,estado):
        try:
            return self.buscar_estado(estado).heuristico
        except AttributeError:
            return 0

    def total_recorrido(self,recorrido):
        costo_recorrido = 0
        if(len(recorrido) == 0 or len(recorrido) == 1): return costo_recorrido
        else:
            for i in range(0,len(recorrido)-1):
                costo_recorrido = costo_recorrido + self.actionCost(self.buscar_estado(recorrido[i]), self.buscar_estado(recorrido[i+1]))
            return costo_recorrido


    def a(self,estado):
        if(estado == Estado('G',0)):
            return 0
        else:
            frontera = {(estado.nombre): estado.heuristico}
            ganador = (estado.nombre)

            while not('G' in ganador):
                minimo = math.inf
                padre = self.buscar_estado(ganador[len(ganador) - 1])
                sucesores = padre.getSucesores()
                del frontera[ganador]
                prototipo = tuple(ganador)
                for s in sucesores:
                    frontera[prototipo + (s.nombre,)] = self.total_recorrido(prototipo + (s.nombre,)) + s.heuristico
                    ganador, minimo = self.seleccionar_ganador(minimo,frontera,ganador)
            return frontera[ganador]


