class Flyweight:

    def operacion(self):
        pass

class ConcreteFlyweight(Flyweight):

    def operacion(self):
        return "Operación del peso ligero concreto clear"

class UnshareFlyweight(Flyweight):

    def __init__(self, concreto, contador):
        self.concreto = concreto
        self.contador = contador

    def operacion(self):
        return self.concreto.operacion() + str(self.contador)

class FlyweightFactory:
    def __init__(self):
        self.concreto = None
        self.contador = 0

    def entregar_flyweight(self):
        if self.concreto == None:
            self.concreto = ConcreteFlyweight()
        self.contador += 1
        return UnshareFlyweight(self.concreto, self.contador)