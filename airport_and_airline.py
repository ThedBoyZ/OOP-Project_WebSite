from dataclasses import dataclass
import numpy as np
import cv2

class Image:
    def __init__(self, filename):
        self.filename = filename
        self.image_data = None
        self.load_image()
    
    def load_image(self):
        self.image_data = cv2.imread(self.filename)

    def get_image_data(self):
        return self.filename
    
    def get_image_size(self):
        height, width, _ = self.image_data.shape
        return height, width
    
    def display_image(self):
        cv2.imshow('Image', self.image_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


@dataclass
class Airline():
    name : str
    logo : Image

class AirlineCollection:
    def __init__(self):
        self.airlines = []
    
    def add_airline(self, name, logo):
        airline = Airline(name, logo)
        self.airlines.append(airline)
    
    def print_airlines(self):
        print("List of Airlines:")
        for airline in self.airlines:
            print(f"{airline.name}")

    def get_airline_image(self, name):
        for airline in self.airlines:
            if airline.name == name:
                return airline.logo.get_image_data()
        return None


@dataclass
class Airport():
    name : str
    abbreviation : str
    terminal : str

class AirportCollection:
    def __init__(self):
        self.airports = []
    
    def add_airport(self, name, abbreviation, terminal):
        airport = Airport(name, abbreviation, terminal)
        self.airports.append(airport)
    
    def get_airport_name(self, abbreviation):
        for airport in self.airports:
            if airport.abbreviation == abbreviation:
                return airport.name
        return None
    
    def print_airports(self):
        print("List of Airports:")
        for airport in self.airports:
            if airport.terminal:
                print(f"{airport.name} ({airport.abbreviation}) - Terminal {airport.terminal}")
            else:
                print(f"{airport.name} ({airport.abbreviation})")

airport_coll = AirportCollection()
airport_coll.add_airport("Suvarnabhumi Airport", "BKK", "")
airport_coll.add_airport("Don Mueang International Airport", "DMK", "Terminal 2")
airport_coll.add_airport("Chiang Mai International Airport", "CNX", "Terminal Domestic")

airline_coll = AirlineCollection()
airline_coll.add_airline("Thai Vietjet Air" , "images/airlines/thai_vietjet_air.png")
airline_coll.add_airline("Bangkok Airways"  , "images/airlines/bangkok_airways.png")
airline_coll.add_airline("Thai Smile Air"   , "images/airlines/thai_smile_air.png")
airline_coll.add_airline("Thai AirAsia"     , "images/airlines/thai_airasia.png")
airline_coll.add_airline("Nok Air"          , "images/airlines/nok_air.png")  
#print(airline_coll.airlines[0].name)            