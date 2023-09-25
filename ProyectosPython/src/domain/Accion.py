import domain.EspacioDeEstados
class Accion:
    def __init__(self, estado1, estado2, costo):
        self.estado1 = estado1
        self.estado2 = estado2
        self.costo = costo

    def getAccion(self):
        return [self.estado2, self.costo]

    def getSucesor(self):
        return self.estado2

    def getPadre(self):
        return self.estado1

    def __str__(self):
        return f"{self.estado1.getNombre()} --> {self.estado2.getNombre()} : {self.costo}"


accion = Accion(domain.Estado('A', 10.7), domain.Estado('B', 6), 10)
a = accion.getAccion()
print("h")
