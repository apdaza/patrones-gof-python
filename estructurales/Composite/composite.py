class Componente():

    def operacion(self):
        pass

class Compuesto(Componente):

    def __init__(self):
        self.__elementos__ = []

    def operacion(self):
        print("operacion de compuesto")
        for e in self.__elementos__:
            e.operacion()

    def agregar_elemento(self, elemento):
        self.__elementos__.append(elemento)

class Simple(Componente):

    def operacion(self):
        print("operacion simple")