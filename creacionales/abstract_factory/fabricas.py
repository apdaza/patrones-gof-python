#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from productos import *

class FabricaAbstracta(ABC):

    @abstractmethod
    def crearMemoria(self):
        pass
    @abstractmethod
    def crearProcesador(self):
        pass
    @abstractmethod
    def crearBoard(self):
        pass

class FabricaAMD(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaAMD()

    def crearProcesador(self):
        return ProcesadorAMD()

    def crearBoard(self):
        return BoardAMD()

class FabricaIntel(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaIntel()

    def crearProcesador(self):
        return ProcesadorIntel()

    def crearBoard(self):
        return BoardIntel()

class FabricaAlien(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaAlien()

    def crearProcesador(self):
        return ProcesadorAlien()

    def crearBoard(self):
        return BoardAlien()
