from .composite import *

class EjemploComposite:
    def obtener_nombre(self):
        return "Composite"

    def operacion(self):
        print("Ejemplo composite")

        elemento = Compuesto()

        for i in range(5):
            elemento.agregar_elemento(Simple())

        elemento2 = Compuesto()
        elemento2.agregar_elemento(Simple())

        elemento.agregar_elemento(elemento2)
        elemento.operacion()