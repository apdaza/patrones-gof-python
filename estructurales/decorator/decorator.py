class Componente():
    def operacion(self):
        pass

class ComponenteConcreto(Componente):
    def operacion(self):
        print("operacion concreta")

class Decorador(Componente):
    def __init__(self, componente):
        self.__comp__ = componente

    def operacion(self):
        pass
    

class DecoradorConcretoA(Decorador):
    def operacion(self):
        print("operacion decorada por A")
        self.__comp__.operacion()

class DecoradorConcretoB(Decorador):
    def operacion(self):
        print("operacion decorada por B")
        self.__comp__.operacion()