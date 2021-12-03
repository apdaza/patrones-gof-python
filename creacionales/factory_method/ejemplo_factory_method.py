from creadores import *

class EjemploFactoryMethod():
    def obtener_nombre(self):
        return "Factory Method"

    def operacion(self):
        creador = CreadorConcreto2()
        producto = creador.crear_producto()
        print(producto.operacion())

if __name__ == "__main__":
    ejemplo = EjemploFactoryMethod()
    ejemplo.operacion()