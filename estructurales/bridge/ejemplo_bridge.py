from .bridge import *

class EjemploBridge:
    def obtener_nombre(self):
        return "Bridge"

    def operacion(self):
        print("Ejemplo bridge")

        objeto = Abstraccion(ImplementadorConcretoB())
        print(objeto.operacion())

        objeto_refinado = AbstraccionRefinada(ImpelmentadorConcretoC())
        print(objeto_refinado.operacion())
        print(objeto_refinado.operacion_refinada())