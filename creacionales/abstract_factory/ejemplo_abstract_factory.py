#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabricas import *

class EjemploAbstractFactory:
    def obtener_nombre(self):
        return "AbstractFactory"

    def operacion(self):
        print("Ejemplo Abstract Factory")
        print("seleccione una fabrica: \n\t " +
              "0 - AMD \n\t " +
              "1 - Intel \n\t " +
              "2 - Alien \n\t " +
              "3 - UD \n\t " +
              "4 - Fusion ")
        fabricas = [FabricaAMD(), FabricaIntel(), FabricaAlien(), FabricaUD(), FabricaFusion()]

        fabrica = fabricas[int(input())]

        partes = [fabrica.crearMemoria(), fabrica.crearProcesador(), 
                  fabrica.crearBoard(), fabrica.crearCooler()]

        for p in partes:
            p.implementacion()
            p.operacion()

if __name__ == '__main__':
    ejemplo = EjemploAbstractFactory()
    ejemplo.operacion()