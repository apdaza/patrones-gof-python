#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creacionales.abstract_factory.ejemplo_abstract_factory import EjemploAbstractFactory
from creacionales.singleton.ejemplo_singleton import EjemploSingleton
from creacionales.prototype.ejemplo_prototype import EjemploPrototype
from estructurales.adapter.ejemplo_adapter import EjemploAdapter
from estructurales.bridge.ejemplo_bridge import EjemploBridge
from estructurales.Composite.ejemplo_composite import EjemploComposite
from estructurales.decorator.ejemplo_decorator import EjemploDecorator


if __name__ == '__main__':
    patrones = [EjemploSingleton(), EjemploAbstractFactory(), EjemploPrototype(), 
                EjemploAdapter(), EjemploBridge(), EjemploComposite(), EjemploDecorator()]
    cont = 0
    for p in patrones:
        print(str(cont) + " -> " + p.obtener_nombre())
        cont += 1

    opcion = int(input("Ingrese una opcion: "))

    ejemplo = patrones[opcion]
    ejemplo.operacion()
