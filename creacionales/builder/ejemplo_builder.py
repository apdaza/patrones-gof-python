from constructores import *

class EjemploBuilder:
    def obtener_nombre(self):
        return "Builder"

    def operacion(self):    
        print("Ejemplo del builder")
        agencia = Agencia(EuropaTour())
        tour = agencia.get_tour()
        tour.mostrar_info()

if __name__ == "__main__":
    ejemplo = EjemploBuilder()
    ejemplo.operacion()