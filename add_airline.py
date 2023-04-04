class Airline:
    def __init__(self, name, logo):
        self.name = name
        self.logo = logo

class AirlineCollection:
    def __init__(self):
        self.airlines = {}
        self.add_airline("Thai Vietjet Air" , "images/airlines/thai_vietjet_air.png")
        self.add_airline("Bangkok Airways"  , "images/airlines/bangkok_airways.png")
        self.add_airline("Thai Smile Air"   , "images/airlines/thai_smile_air.png")
        self.add_airline("Thai AirAsia"     , "images/airlines/thai_airasia.png")
        self.add_airline("Nok Air"          , "images/airlines/nok_air.png")
    
    def add_airline(self, name, logo_file):
        if name in self.airlines:
            raise ValueError("Airline already exist")
        self.airlines[name] = Airline(name, logo_file)
    
    def remove_airline(self, name):
        if name not in self.airlines:
            raise ValueError("Airline does not exist")
        del self.airlines[name]
    
    def print_airlines(self):
        print("List of Airlines:")
        for airline in self.airlines.values():
            print(f"{airline.name}")


if __name__ == "__main__":

    # Creating an instance of AirlineCollection
    airline_collection = AirlineCollection()

    # Adding an airline
    airline_collection.add_airline("Thai Lion Air", "images/airlines/thai_lion_air.png")

    # Printing the list of airlines
    airline_collection.print_airlines()