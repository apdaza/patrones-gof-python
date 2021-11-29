#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Memoria(ABC):
    def implementacion(self):
        print("instalando memoria")

    @abstractmethod
    def operacion(self):
        pass

class Board(ABC):
    def implementacion(self):
        print("instalando board")

    @abstractmethod
    def operacion(self):
        pass

class Procesador(ABC):
    def implementacion(self):
        print("instalando procesador")

    @abstractmethod
    def operacion(self):
        pass

class Cooler(ABC):
    def implementacion(self):
        print("instalando cooler")

    @abstractmethod
    def operacion(self):
        pass

class MemoriaAMD(Memoria):

    def operacion(self):
        print("operando memoria AMD")

class BoardAMD(Board):

    def operacion(self):
        print("operando board AMD")

class ProcesadorAMD(Procesador):

    def operacion(self):
        print("operando procesador AMD")

class CoolerAMD(Cooler):    

    def operacion(self):
        print("operando cooler AMD")

class MemoriaIntel(Memoria):

    def operacion(self):
        print("operando memoria Intel")

class BoardIntel(Board):

    def operacion(self):
        print("operando board Intel")

class ProcesadorIntel(Procesador):

    def operacion(self):
        print("operando procesador Intel")

class CoolerIntel(Cooler):

    def operacion(self):
        print("operando cooler Intel")

class MemoriaAlien(Memoria):

    def operacion(self):
        print("operando memoria Alien")

class BoardAlien(Board):

    def operacion(self):
        print("operando board Alien")

class ProcesadorAlien(Procesador):
    
    def operacion(self):
        print("operando procesador Alien")

class CoolerAlien(Cooler):

    def operacion(self):
        print("operando cooler Alien")

class MemoriaUD(Memoria):

    def operacion(self):
        print("operando memoria UD")

class BoardUD(Board):

    def operacion(self):
        print("operando board UD")

class ProcesadorUD(Procesador):
    
    def operacion(self):
        print("operando procesador UD")

class CoolerUD(Cooler):

    def operacion(self):
        print("operando cooler UD")

class MemoriaFusion(Memoria):

    def operacion(self):
        print("operando memoria Fusion")

class BoardFusion(Board):
    
    def operacion(self):
        print("operando board Fusion")

class ProcesadorFusion(Procesador):
    
    def operacion(self):
        print("operando procesador Fusion")

class CoolerFusion(Cooler):
    
    def operacion(self):
        print("operando cooler Fusion")

class MemoriaRazer(Memoria):

    def operacion(self):
        print("operando memoria Razer")

class BoardRazer(Board):

    def operacion(self):    
        print("operando board Razer")

class ProcesadorRazer(Procesador):

    def operacion(self):
        print("operando procesador Razer")

class CoolerRazer(Cooler):

    def operacion(self):
        print("operando cooler Razer")