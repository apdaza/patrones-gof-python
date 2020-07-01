class Abstraccion():
    def __init__(self, implementador):
        self.__imp__ = implementador

    def operacion(self):
        return self.__imp__.operacion_implementada()

class AbstraccionRefinada(Abstraccion):

    def operacion_refinada(self):
        return self.__imp__.operacion_implementada_refinada()

class Implementador():
    def operacion_implementada(self):
        pass

class ImplementadorRefinado(Implementador):
    def operacion_implementada_refinada(self):
        pass

class ImplementadorConcretoA(Implementador):

    def operacion_implementada(self):
        return "operacion concreta A"

class ImplementadorConcretoB(Implementador):

    def operacion_implementada(self):
        return "operacion concreta B"

class ImpelmentadorConcretoC(ImplementadorRefinado):

    def operacion_implementada(self):
        return "operacion concreta C"

    def operacion_implementada_refinada(self):
        return "operacion refinada C"