class Booking:
    def __init__(self, status, typestavel):
        self.__status = status
        self.__typestavel = typestavel

class Airport:
    def __init__(self, province_name, country_name, abbreviation):
        self.__province_name = province_name
        self.__country_name = country_name
        self.__abbreviation = abbreviation

class Flight:
    def __init__(self, type_trip, id, baggage, refund, reschedule, status, \
        departure_airport, departure_date , departure_time, arrival_airport , arrival_date , arrival_time , tax):
        self.type_trip = type_trip
        self.id = id
        self.baggage = baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport = departure_airport
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_airport = arrival_airport
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.tax = tax

class Collection:
    def __init__(self, flight, count_transit):
        self._flight = flight
        self.__count_transit = count_transit

class Airline:
    def __init__(self, name , logo):
        self.name = name
        self.logo = logo
