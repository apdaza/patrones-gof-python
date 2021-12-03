
class Tour():
    def __init__(self, name):
        self.name = name
        self.places = []
        self.hotels = []

    def add_place(self, place): 
        self.places.append(place)

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def mostrar_info(self):
        print("Tour:", self.name)
        print("Places:", self.places)
        print("Hotels:", self.hotels)

   

