import abc


from abc import ABC, abstractmethod
from tour import Tour

class ConstructorTour(ABC):
    @abstractmethod
    def construir_tour(self):
        pass

    @abstractmethod
    def agregar_hoteles(self):
        pass

    @abstractmethod
    def agregar_lugares(self):
        pass

    def get_tour(self):
        return self.tour

class CundinamarcaTour(ConstructorTour):
    def construir_tour(self):
        self.tour = Tour("Cundinamarca")
        
    def agregar_hoteles(self):
        self.tour.add_hotel("Bogotá Inn")
        self.tour.add_hotel("La Mesa Inn")
        self.tour.add_hotel("Zipa Inn")

    def agregar_lugares(self):
        self.tour.add_place("Bogotá")
        self.tour.add_place("La Mesa")
        self.tour.add_place("Zipaquirá")

class EuropaTour(ConstructorTour):
    def construir_tour(self):
        self.tour = Tour("Europa")
        
    def agregar_hoteles(self):
        self.tour.add_hotel("Paris Inn")
        

    def agregar_lugares(self):
        self.tour.add_place("Torre Eiffel")
        self.tour.add_place("Louvre")
        self.tour.add_place("Arc de Triomphe")

class Agencia():
    def __init__(self, construtor):
        self.constructor = construtor
        self.constructor.construir_tour()
        self.constructor.agregar_hoteles()
        self.constructor.agregar_lugares()
        
    def get_tour(self):
        return self.constructor.get_tour()