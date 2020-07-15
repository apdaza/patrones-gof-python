class Subject:

    def peticion(self):
        pass

class RealSubject(Subject):

    def peticion(self):
        return "operación del objeto real"

class Proxy(Subject):
    def __init__(self, objeto):
        self.objeto = objeto

    def peticion(self):
        return "Mediante el proxy -> " + self.objeto.peticion()