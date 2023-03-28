from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Trip(list):
    
    def search_flight(self, airline_name, day):
        matching_flights = []
        for flight in Flight.all_flight:
            if airline_name == flight[0]:
              if day == flight[1]:
                matching_flights.append(flight)
                print(flight)
        #return matching_flights
    
    def search_flight1(self):
        print("1")
    
    def add_flight():
        pass
    
class Flight:
   
    all_flight = Trip()

    def __init__(self, airline, day, departure_airport, departure_day, departure_time, arrival_airport, arrival_day, arrival_time, baggage , refund, id, status) -> None:
        self.airline = airline
        self.day = day
        self.departure_airport = departure_airport
        self.departure_day = departure_day
        self.departure_time = departure_time
        self.arrival_airport = arrival_airport
        self.arrival_day = arrival_day
        self.arrival_time = arrival_time
        self.baggage = baggage
        self.refund = refund
        self.id = id
        self.status = status
        self.airline = airline
        self.detail = []

        self.detail.append(airline)
        self.detail.append(day)
        self.detail.append(departure_airport)
        self.detail.append(departure_day)
        self.detail.append(departure_time)
        self.detail.append(arrival_airport)
        self.detail.append(arrival_day)
        self.detail.append(arrival_time)
        self.detail.append(baggage)
        self.detail.append(refund)
        self.detail.append(id)


        self.all_flight.append(self.detail)

airline = ["Thai Vietjet Air", "Thai AirAsia", "Thai Smile Air", "Bangkok Airways"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
departure_airport = ["BKK","DMK","PHS","CNX","HKT","HDY","UTH","CEI","KKC","KBV","UBP","NST","URT","KOP"]
arrival_airport = ["BKK","DMK","PHS","CNX","HKT","HDY","UTH","CEI","KKC","KBV","UBP","NST","URT","KOP"]
id_Vietjet = ["VZ100","VZ102","VZ104","VZ106","VZ110","VZ114","VZ2104","VZ2106","VZ2114","VZ118","VZ120","VZ122"]
id_AirAsia = ["FD4100","FD4104","FD4106"]
id_Smile_Air = ["WE102","WE104","WE108","WE110","WE120","WE164",]
id_Bangkok = ["PG215","PG217","PG219","PG223"]
baggage = 7
refund = False
status = ["One Way","Round Trip"]

vietjet_flight_ids = {
    "06:10": "VZ100",
    "07:40": "VZ114",
    "10:00": "VZ102",
    "12:40": "VZ104",
    "14:25": "VZ106",
    "15:30": "VZ110",
    "15:35": "VZ120",
    "18:00": "VZ2104",
    "19:40": "VZ118",
    "20:40": "VZ2106",
    "21:30": "VZ2114"
}

departure_times_BKK_to_CNX = {
    'Monday': ["06:10", "10:00", "12:40", "14:25", "15:30", "18:00", "20:40", "21:30"],
    'Tuesday': ["06:10", "07:40", "20:40", "21:30"],
    'Wednesday': ["06:10", "12:40", "14:25", "15:35", "18:00","20:40", "21:30"],
    'Thursday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"],
    'Friday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "20:40", "21:30"],
    'Saturday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"],
    'Sunday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"]
}

arrival_times_BKK_to_CNX = {
    'Monday': ["07:25", "11:15", "13:55", "15:40", "16:45", "19:15", "21:55", "22:45"],
    'Tuesday': ["07:25", "08:55", "21:55", "22:45"],
    'Wednesday': ["07:25", "16:45", "16:50", "16:50", "19:15","21:55","22:45"],
    'Thursday': ["07:25", "08:55", "11:15", "13:55", "15:40", "16:45", "19:15", "20:55", "21:55", "22:45"],
    'Friday': ["07:25", "08:55", "11:15", "13:55", "15:40", "16:45", "19:15", "21:55", "22:45"],
    'Saturday': ["07:25", "08:55", "11:15", "13:55", "15:40", "16:45", "19:15", "20:55", "21:55", "22:45"],
    'Sunday': ["07:25", "08:55", "11:15", "13:55", "15:40", "16:45", "19:15", "20:55", "21:55", "22:45"]
}

flights = []

for day, departure_list in departure_times_BKK_to_CNX.items():
    arrival_list = arrival_times_BKK_to_CNX[day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline[0], day, departure_airport[0], None, departure_list[i], arrival_airport[3], None, arrival_list[i], baggage, refund, id_Vietjet, status[0])
       


my_trip = Trip()
search,travelday = input().split("/")
#my_trip.search_flight("air asia")
print(my_trip.search_flight(search,travelday))
#print(Flight.all_flight)

#print(Flight1.name)
#print(Trip().search_flight("air asia"))
# bkk_to_cnx = Flight('000001', 7, False, False, True, 'BKK', 'Sunday', '15:00', 'CNX', 'Sunday', '17:10', 'Thai Vietjet Air')
# cnx_to_bkk = Flight('000002', 7, False, False, True, 'CNX', 'Monday', '10:00', 'BKK', 'Monday', '11:30', 'Thai Vietjet Air')


#print(Flight1.name)