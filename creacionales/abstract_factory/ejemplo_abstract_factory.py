#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabricas import *

class EjemploAbstractFactory:

    def operacion(self):
        print "Ejemplo Abstract Factory"
        print "seleccione una fabrica: \n\t 0 - AMD \n\t 1 - Intel "
        fabricas = [FabricaAMD(), FabricaIntel()]

        fabrica = fabricas[input()]

        partes = [fabrica.crearMemoria(), fabrica.crearProcesador(), fabrica.crearBoard()]

        for p in partes:
            print p.operacion()
