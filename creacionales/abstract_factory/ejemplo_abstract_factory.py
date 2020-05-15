#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabricas import *

class EjemploAbstractFactory:

    def operacion(self):
        print("Ejemplo Abstract Factory")
        print("seleccione una fabrica: \n\t 0 - AMD \n\t 1 - Intel \n\t 2 - Alien ")
        fabricas = [FabricaAMD(), FabricaIntel(), FabricaAlien()]

        fabrica = fabricas[int(input())]

        partes = [fabrica.crearMemoria(), fabrica.crearProcesador(), fabrica.crearBoard()]

        for p in partes:
            p.implementacion()
            
            print(p.operacion())


ejemplo = EjemploAbstractFactory()

ejemplo.operacion()