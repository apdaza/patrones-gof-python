from .chain_of_responsability import *

class EjemploCadena:
    def obtener_nombre(self):
        return "Chain of responsability"

    def operacion(self):
        cadena = [HandlerOptionSix(), HandlerOptionTwo(), HandlerOptionThree(), HandlerOptionFour(),
                  HandlerOptionFive(), HandlerOptionOne(), HandlerOptionSeven(), HandlerOptionDefault()]

        for i in range(len(cadena)-1):
            cadena[i].set_succesor(cadena[i+1])

        opcion = int(input("ingrese un número: "))
        cadena[0].handler_request(opcion)

