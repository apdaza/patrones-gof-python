from singleton import Singleton

class EjemploSingleton:

    def operacion(self):
        print "Ejemplo Singleton"
        x = Singleton.get_instance()
        y = Singleton.get_instance()

        print x is y
