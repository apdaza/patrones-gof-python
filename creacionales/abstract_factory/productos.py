#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Memoria:

    def operacion(self):
        pass

class Board:

    def operacion(self):
        pass

class Procesador:

    def operacion(self):
        pass

class MemoriaAMD(Memoria):

    def operacion(self):
        print "operando memoria AMD"

class BoardAMD(Board):

    def operacion(self):
        print "operando board AMD"

class ProcesadorAMD(Procesador):

    def operacion(self):
        print "operando procesador AMD"

class MemoriaIntel(Memoria):

    def operacion(self):
        print "operando memoria Intel"

class BoardIntel(Board):

    def operacion(self):
        print "operando board Intel"

class ProcesadorIntel(Procesador):

    def operacion(self):
        print "operando procesador Intel"
