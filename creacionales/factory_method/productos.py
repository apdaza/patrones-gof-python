from abc import ABC, abstractmethod

class Producto(ABC):
    
    @abstractmethod
    def operacion(self):
        pass

class ProductoConcreto1(Producto):
    
    def operacion(self):
        return "Operacion de Producto concreto 1"

class ProductoConcreto2(Producto):
    
    def operacion(self):
        return "Operacion de Producto concreto 2"