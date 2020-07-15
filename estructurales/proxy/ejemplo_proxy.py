from .proxy import *

class EjemploProxy:
    def obtener_nombre(self):
        return "Proxy"

    def operacion(self):
        print("Ejemplo proxy")

        proxy = Proxy(RealSubject())

        print(proxy.peticion())