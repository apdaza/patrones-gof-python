from .decorator import *

class EjemploDecorator:
    def obtener_nombre(self):
        return "Decorator"

    def operacion(self):
        print("Ejemplo decorator")

        objeto = ComponenteConcreto()
        objeto.operacion()
        print("-"*10)
        decorador1 = DecoradorConcretoA(objeto)
        decorador1.operacion()
        print("-"*10)
        decorador2 = DecoradorConcretoB(decorador1)
        decorador2.operacion()