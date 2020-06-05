#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .fabrica import AnimalCreator

class EjemploPrototype:
    def obtener_nombre(self):
        return "Prototype"

    def operacion(self):
        print("Ejemplo prototype")
        creator = AnimalCreator()
        animals = []
        for i in range(4):
            animals.append(creator.retrieve_animal("Chicken"))
        for i in range(4):
            animals.append(creator.retrieve_animal("Sheep"))

        for i in animals:
            print(i.hello_animal())

        animals[4].change_owner("Alejandro")

        for i in animals:
            print(i.hello_animal())