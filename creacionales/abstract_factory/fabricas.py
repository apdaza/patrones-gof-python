#!/usr/bin/env python
# -*- coding: utf-8 -*-

from productos import *

class FabricaAbstracta:

    def crearMemoria(self):
        pass

    def crearProcesador(self):
        pass

    def crearBoard(self):
        pass

class FabricaAMD:

    def crearMemoria(self):
        return MemoriaAMD()

    def crearProcesador(self):
        return ProcesadorAMD()

    def crearBoard(self):
        return BoardAMD()

class FabricaIntel:

    def crearMemoria(self):
        return MemoriaIntel()

    def crearProcesador(self):
        return ProcesadorIntel()

    def crearBoard(self):
        return BoardIntel()
