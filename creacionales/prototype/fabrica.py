#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .prototipos import Sheep, Chicken, Owner

class AnimalCreator():
    def __init__(self):
        self.__chicken__ = Chicken()
        self.__sheep__ = Sheep()
        
        self.__chicken__.set_owner(Owner("Juan"))
        self.__chicken__.set_description("a litle chicken")
        self.__chicken__.set_name("chicken")
        self.__chicken__.set_number_of_legs(2)
        
        self.__sheep__.set_owner(Owner("Juan"))
        self.__sheep__.set_description("a litle sheep")
        self.__sheep__.set_name("sheep")
        self.__sheep__.set_number_of_legs(4)

    def retrieve_animal(self, kind_of_animal):
        if "Chicken" == kind_of_animal:
            return self.__chicken__.clone()
        elif "Sheep" == kind_of_animal:
            return self.__sheep__.clone()
        return None