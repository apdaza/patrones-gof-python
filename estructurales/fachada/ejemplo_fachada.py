from .fachada import *

class EjemploFachada:
    def obtener_nombre(self):
        return "Fachada"

    def operacion(self):
        print("Ejemplo fachada")

        fachada = Fachada()

        print(fachada.buscar_libros())
        print(fachada.buscar_musica())
        print(fachada.buscar_videos())
        