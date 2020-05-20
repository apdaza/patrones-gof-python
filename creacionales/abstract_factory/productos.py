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

class MemoriaAMD(Memoria):

    def operacion(self):
        print("operando memoria AMD")

class BoardAMD(Board):

    def operacion(self):
        print("operando board AMD")

class ProcesadorAMD(Procesador):

    def operacion(self):
        print("operando procesador AMD")

class MemoriaIntel(Memoria):

    def operacion(self):
        print("operando memoria Intel")

class BoardIntel(Board):

    def operacion(self):
        print("operando board Intel")

class ProcesadorIntel(Procesador):

    def operacion(self):
        print("operando procesador Intel")

class MemoriaAlien(Memoria):

    def operacion(self):
        print("operando memoria Alien")

class BoardAlien(Board):

    def operacion(self):
        print("operando board Alien")

class ProcesadorAlien(Procesador):
    
    def operacion(self):
        print("operando procesador Alien")