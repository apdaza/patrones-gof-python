class Adaptado():

    def escribir_reves(self):
        return "retpada ed olpmeje nU"

class Objetivo():

    def escribir(self):
        pass

class Original(Objetivo):

    def escribir(self):
        return "Un ejemplo de adapter"

class Adaptador(Objetivo):

    def __init__(self):
        self.__adaptado__ = Adaptado()
    
    def escribir(self):
        return "(Traduccion) " + ((self.__adaptado__.escribir_reves())[::-1])
