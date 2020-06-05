#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from copy import copy, deepcopy

class Animal(ABC):
    
    def __init__(self):
        self.__description__ = ""
        self.__number_of_legs__ = 0
        self.__name__ = ""
        self.__owner__ = None

    def hello_animal(self):
        return "hi i am a " + self.__name__ + " and i have " + str(self.__number_of_legs__) + " legs, property of: " + self.__owner__.get_name()

    def set_owner(self, owner):
        self.__owner__ = owner;

    def get_owner(self):
        return self.__owner__
    
    def change_owner(self, name):
        self.__owner__.set_name(name)
    

    def set_description(self, description):
        self.__description__ = description;
    
    def get_description(self):
        return self.__description__

    def get_name(self):
        return self.__name__

    def set_name(self, name):
        self.__name__ = name;

    def get_number_of_legs(self):
        return self.__number_of_legs__

    def set_number_of_legs(self, number_of_legs):
        self.__number_of_legs__ = number_of_legs

    def clone(self):
        return deepcopy(self)

class Sheep(Animal):
    pass

class Chicken(Animal):
    pass

class Owner():

    def __init__(self, name):
        self.__name__ = name

    def get_name(self):
        return self.__name__;
    
    def set_name(self, name):
        self.__name__ = name;

