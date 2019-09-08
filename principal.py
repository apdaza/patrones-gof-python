from creacionales.singleton.ejemplo_singleton import EjemploSingleton

opcion = input("Ingrese una opcion: ")

if opcion == 0:
    ejemplo = EjemploSingleton()
    ejemplo.operacion()
