#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creacionales.abstract_factory.ejemplo_abstract_factory import EjemploAbstractFactory
from creacionales.singleton.ejemplo_singleton import EjemploSingleton
from creacionales.prototype.ejemplo_prototype import EjemploPrototype
from estructurales.adapter.ejemplo_adapter import EjemploAdapter


if __name__ == '__main__':
    patrones = [EjemploSingleton(), EjemploAbstractFactory(), EjemploPrototype(), 
                EjemploAdapter()]
    cont = 0
    for p in patrones:
        print(str(cont) + " -> " + p.obtener_nombre())
        cont += 1

    opcion = int(input("Ingrese una opcion: "))

    ejemplo = patrones[opcion]
    ejemplo.operacion()
