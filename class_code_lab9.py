class Airport:
    def __init__(self, province_name, country_name, abbreviation):
        self.__province_name = province_name
        self.__country_name = country_name
        self.__abbreviation = abbreviation

bkk = Airport('Bangkok', 'Thailand', 'BKK')
cnx = Airport('Chiang Mai', 'Thailand', 'CNX')
    
class Airline:
    def __init__(self, name , logo):
        self.name = name
        self.logo = logo

air_asia = Airline('Air Asia', 'logo1')
nok_air = Airline('Nok Air', 'logo2')

class Flight:
    def __init__(self, type_trip, id, baggage, refund, reschedule, status, \
        departure_day , departure_time, arrival_day , arrival_time):
        self.type_trip = type_trip
        self.id = id
        self.baggage = baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport = Airport
        self.departure_date = departure_day
        self.departure_time = departure_time
        self.arrival_airport = Airport
        self.arrival_date = arrival_day
        self.arrival_time = arrival_time
        self.airline = Airline

bkk_to_cnx = Flight('000001', 7, False, False, True, 'BKK', 'Sunday', '15:00', 'CNX', 'Sunday', '17:10', 'Thai Vietjet Air')
cnx_to_bkk = Flight('000002', 7, False, False, True, 'CNX', 'Monday', '10:00', 'BKK', 'Monday', '11:30', 'Thai Vietjet Air')

class Trip:
    def __init__(self):
        self.flight_list = []
        self.count_transit = 0
    def count_flight(self, transit):
        self.count_transit += transit
    def add_flight(self, flight):
        self.flight_list.add(flight)

trip1 = Trip(1)
trip1.add_flight(bkk_to_cnx)
trip1.add_flight(cnx_to_bkk)