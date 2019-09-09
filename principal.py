#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creacionales.singleton.ejemplo_singleton import EjemploSingleton
from creacionales.abstract_factory.ejemplo_abstract_factory import EjemploAbstractFactory

def obtener_patron(opcion):
    patrones = [EjemploSingleton(),EjemploAbstractFactory()]
    return patrones[opcion]


if __name__ == '__main__':
    opcion = input("Ingrese una opcion: ")

    ejemplo = obtener_patron(opcion)
    ejemplo.operacion()
