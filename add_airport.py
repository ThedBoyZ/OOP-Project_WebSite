class Airport:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation

class AirportCollection:
    def __init__(self):
        self.airports = {}
        self.add_airport("Suvarnabhumi Airport", "BKK")
        self.add_airport("Don Mueang International Airport", "DMK")
        self.add_airport("Chiang Mai International Airport", "CNX")
    
    def add_airport(self, name, abbreviation):
        if name in self.airports:
            raise ValueError("Airport already exist")
        self.airports[name] = Airport(name, abbreviation)

    def remove_airport(self, name):
        if name not in self.airports:
            raise ValueError("Airport does not exist")
        del self.airports[name]
    
    def print_airports(self):
        print("List of Airports:")
        for airport in self.airports.values():
            print(f"{airport.name} ({airport.abbreviation})")


if __name__ == "__main__":

    # Creating an instance of AirlineCollection
    airport_collection = AirportCollection()

    # Adding an airline
    airport_collection.add_airport("Phuket International Airport", "HKT")

    # Printing the list of airlines
    airport_collection.print_airports()