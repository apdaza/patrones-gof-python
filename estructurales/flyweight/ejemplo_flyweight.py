from .flyweight import *

class EjemploFlyweight:
    def obtener_nombre(self):
        return "Flyweight"

    def operacion(self):
        print("Ejemplo flyweight")

        factoria = FlyweightFactory()

        flyweights = []

        for i in range(10):
            flyweights.append(factoria.entregar_flyweight())

        print(flyweights[0].concreto == flyweights[2].concreto)
        
        for f in flyweights:
            print(f.operacion())