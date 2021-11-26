from .adapter import *

class EjemploAdapter:
    def obtener_nombre(self):
        return "Adapter"

    def operacion(self):
        print("Ejemplo adapter")

        print("Objeto original")
        original = Original()
        print(original.escribir())

        print("Objeto a adaptar")
        adaptado = Adaptado()
        print(adaptado.escribir_reves())

        print("Objeto adaptado")
        adaptador = Adaptador()
        print(adaptador.escribir())

