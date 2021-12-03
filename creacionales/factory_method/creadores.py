from abc import ABC, abstractmethod

from productos import *

class Creador(ABC):
    
    def crear_producto(self):
        return self.factory_method()

    @abstractmethod
    def factory_method(self):
        pass

class CreadorConcreto1(Creador):

    def factory_method(self):
        return ProductoConcreto1()

class CreadorConcreto2(Creador):

    def factory_method(self):
        return ProductoConcreto2()