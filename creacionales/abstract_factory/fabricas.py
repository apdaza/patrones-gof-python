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

    @abstractmethod
    def crearCooler(self):
        pass

class FabricaAMD(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaAMD()

    def crearProcesador(self):
        return ProcesadorAMD()

    def crearBoard(self):
        return BoardAMD()

    def crearCooler(self):
        return CoolerAMD()

class FabricaIntel(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaIntel()

    def crearProcesador(self):
        return ProcesadorIntel()

    def crearBoard(self):
        return BoardIntel()

    def crearCooler(self):
        return CoolerIntel()

class FabricaAlien(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaAlien()

    def crearProcesador(self):
        return ProcesadorAlien()

    def crearBoard(self):
        return BoardAlien()
    
    def crearCooler(self):
        return CoolerAlien()

class FabricaUD(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaUD()

    def crearProcesador(self):
        return ProcesadorUD()

    def crearBoard(self):
        return BoardUD()

    def crearCooler(self):
        return CoolerUD()

class FabricaFusion(FabricaAbstracta):

    def crearMemoria(self):
        return MemoriaFusion()

    def crearProcesador(self):
        return ProcesadorFusion()

    def crearBoard(self):
        return BoardFusion()

    def crearCooler(self):
        return CoolerFusion()
