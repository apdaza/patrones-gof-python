from .command import *

class EjemploCommand:
    def obtener_nombre(self):
        return "Command"

    def operacion(self):
        comandos = [Politician(), DomesticEngineer(), Programmer()]
        r = Recivier()
        for i in comandos:
            i.execute(r)