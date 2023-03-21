from abc import ABC, abstractmethod
from dataclasses import dataclass

class Trip(list):
    
    def search_flight(self, name):
        matching_flight = []
        for flight in Flight.all_flight:
            if name in flight:
                matching_flight.append(name)
        return matching_flight
    
    def search_flight1(self):
        print("1")
    
    def add_flight()

        
class Flight:
   
    all_flight = Trip()

    def __init__(self, name, day, destination) -> None:
        self.name = name
        self.day = day
        self.destination = destination
        self.detail = []

        self.detail.append(name)
        self.detail.append(day)
        self.detail.append(destination)


        self.all_flight.append(self.detail)

Flight1 = Flight("air asia", "Monday", "CNX")
Flight2 = Flight("Nok air", "Tuesday", "CNX")
Flight3 = Flight("air asia", "Wednesday", "CNX")


# bkk_to_cnx = Flight('000001', 7, False, False, True, 'BKK', 'Sunday', '15:00', 'CNX', 'Sunday', '17:10', 'Thai Vietjet Air')
# cnx_to_bkk = Flight('000002', 7, False, False, True, 'CNX', 'Monday', '10:00', 'BKK', 'Monday', '11:30', 'Thai Vietjet Air')


#print(Flight1.name)
print(Flight.all_flight)
#print(Trip().search_flight("air asia"))
