from .interpreter import *

class EjemploInterpreter:
    def obtener_nombre(self):
        return "Interpreter"

    def operacion(self):
        operacion = ExpresionPluss(left=ExpresionNumber(value='15'),right=ExpresionMinus(left=ExpresionNumber(value='25'), right=ExpresionNumber(value='5')))

        print(operacion.evaluate())