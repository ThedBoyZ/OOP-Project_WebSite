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
        self.add_airport("Phuket International Airport", "HKT")
        self.add_airport("Hat Yai International Airport", "HDY")
        self.add_airport("Udon Thani International Airport", "UTH")
        self.add_airport("Khon Kaen Airport", "KKC")
        self.add_airport("Chiang Rai International Airport", "CEI")
        self.add_airport("Krabi Airport", "KBV")
        self.add_airport("Ubon Ratchathani Airport", "UBP")
        self.add_airport("Nakhon Si Thammarat Airport", "NST")
        self.add_airport("Surat Thani International Airport", "URT")
        self.add_airport("Roi Et Airport", "ROI")
        self.add_airport("Samui International Airport", "USM")
        self.add_airport("Nakhon Phanom Airport", "KOP")
        self.add_airport("Trang Airport", "TST")
    
    def add_airport(self, name, abbreviation):
        if abbreviation in self.airports:
            raise ValueError("Airport already exist")
        self.airports[abbreviation] = Airport(name, abbreviation)

    def remove_airport(self, abbreviation):
        if abbreviation not in self.airports:
            raise ValueError("Airport does not exist")
        del self.airports[abbreviation]
    
    def print_airports(self):
        print("List of Airports:")
        for airport in self.airports.values():
            print(f"{airport.name} ({airport.abbreviation})")


if __name__ == "__main__":

    # Creating an instance of AirlineCollection
    airport_collection = AirportCollection()
    print(airport_collection.airports["BKK"].name)