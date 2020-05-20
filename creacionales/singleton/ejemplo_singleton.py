from .singleton import Singleton

class EjemploSingleton:
    def obtener_nombre(self):
        return "Singleton"

    def operacion(self):
        print("Ejemplo Singleton")
        x = Singleton.get_instance()
        y = Singleton.get_instance()

        print( x is y)