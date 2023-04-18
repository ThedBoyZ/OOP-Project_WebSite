from abc import ABC, abstractmethod
from dataclasses import dataclass
from airport_and_airline import AirlineCollection,AirportCollection

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

flights = []

class Trip():

    @staticmethod
    def search_flight(departure, arrival, day):
        matching_flights = []
        for flight in Flight.all_flight:
            if departure == flight["departure_airport"] and arrival == flight["arrival_airport"] and day == flight["day"] :
                matching_flights.append(flight)
        #         print(flight)
        # print("\n")
        return matching_flights
    
    @staticmethod
    def search_airline(airline_name, day):
        matching_airlines = []
        for flight in Flight.all_flight:
            if airline_name == flight[0] and day == flight[1] :
                matching_airlines.append(flight)
        #         print(flight)
        # print("\n")
        return matching_airlines

    
    # def search_airline(self, airline_name, day):
    #     matching_flights = []
    #     for flight in Flight.all_flight:
    #         if airline_name == flight[0]:
    #           if day == flight[1]:
    #             matching_flights.append(flight)
    #             print(flight)
    #     print("\n")
    #     return matching_flights
    
class Flight:
   
    all_flight = []
    def __init__(self, airline, day, departure_airport, departure_day, departure_time, arrival_airport, arrival_day, arrival_time, baggage , refund, reschedule, id, status) -> None:
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
        self.reschedule = reschedule
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
        self.detail.append(reschedule)
        self.detail.append(id)
        self.detail = self.get_flight_detail()

        Flight.all_flight.append(self.detail)
    
    def get_flight_detail(self):
        return {
            "flight_id": self.id,
            "airline_name": self.airline,
            "day": self.day,
            "departure_date": self.departure_day,
            "departure_time": self.departure_time,
            "arrival_date": self.arrival_day,
            "arrival_time": self.arrival_time,
            "departure_airport": self.departure_airport,
            "arrival_airport": self.arrival_airport,
            "cabin_baggage": self.baggage,
            "refund": self.refund,
            "reschedule": self.reschedule,
            "status": self.status
        }
class Element_Details_Flight:
    def __init__(self, day, departure_airport, arrival_airport, id_Vietjet, id_AirAsia, id_Smile_Air, id_Bangkok, baggage, refund, reschedule, status):
        self.day = day
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.id_Vietjet = id_Vietjet
        self.id_AirAsia = id_AirAsia
        self.id_Smile_Air = id_Smile_Air
        self.id_Bangkok = id_Bangkok
        self.baggage = baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
# ,"CEI","KKC","KBV","UBP","NST","URT","KOP"
element_details1 = Element_Details_Flight(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ["BKK","DMK","PHS","CNX","HKT","HDY","UTH"],
    ["BKK","DMK","PHS","CNX","HKT","HDY","UTH"],
    ["VZ100","VZ102","VZ104","VZ106","VZ110","VZ114","VZ2104","VZ2106","VZ2114","VZ118","VZ120","VZ122","VZ300","VZ305","VZ306","VZ308","VZ310","VZ312","VZ314","VZ315","VZ316","VZ317","VZ2300","VZ2304"],
    ["FD4100","FD4104","FD4106"],
    ["WE102","WE104","WE108","WE110","WE120","WE164"],
    ["PG215","PG217","PG219","PG223"],
    [7,20],
    False,
    True,
    ["One Way","Round Trip"]
)

# *
# ***
# instance of All flight
# ***
# *

################## Vietjet Bangkok to Chiang Mai##########################
i = "01:15"
# Time Revival
vietjet_flight_ids = {
    "06:10": "VZ100",  "07:40": "VZ114",  "08:00": "VZ317",  "08:55": "VZ315",  "10:00": "VZ102",  "12:40": "VZ104",
    "14:25": "VZ106",  "15:30": "VZ110",  "15:35": "VZ120",  "18:00": "VZ2104",
    "19:40": "VZ118",  "20:40": "VZ2106", "21:30": "VZ2114"
}

departure_VietJet_BKK_to_CNX = {
    'Monday': ["06:10", "10:00", "12:40", "14:25", "15:30", "18:00", "20:40", "21:30"],
    'Tuesday': ["06:10", "07:40", "20:40", "21:30"],
    'Wednesday': ["06:10", "12:40", "14:25", "15:35", "18:00","20:40", "21:30"],
    'Thursday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"],
    'Friday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "20:40", "21:30"],
    'Saturday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"],
    'Sunday': ["06:10", "07:40", "10:00", "12:40", "14:25", "15:30", "18:00", "19:40", "20:40", "21:30"]
}

arrival_VietJet_BKK_to_CNX = {
   'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_CNX['Sunday']]
}

for element_details1.day , departure_list in departure_VietJet_BKK_to_CNX.items():
    arrival_list = arrival_VietJet_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_Vietjet, element_details1.status[0])
################## BangkokAir Bangkok to Chiang Mai##########################
i = "01:20"
# Time Revival
bangkok_flight_ids = {
    "08:00": "PG215", "09:55": "PG223", "12:25": "PG217", "17:50": "PG219"
}

departure_Bangkok_BKK_to_CNX = {
    'Monday': ["08:00", "09:55", "12:25", "17:50"],
    'Tuesday': ["08:00", "09:55", "12:25", "17:50"],
    'Wednesday': ["08:00", "09:55", "12:25", "17:50"],
    'Thursday': ["08:00", "09:55", "12:25", "17:50"],
    'Friday': ["08:00", "09:55", "12:25", "17:50"],
    'Saturday': ["08:00", "09:55", "12:25", "17:50"],
    'Sunday': ["08:00", "09:55", "12:25", "17:50"]
}

arrival_Bangkok_BKK_to_CNX = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Sunday']]
}

for element_details1.day , departure_list in departure_Bangkok_BKK_to_CNX.items():
    arrival_list = arrival_Bangkok_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Bangkok = bangkok_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[1].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Bangkok, element_details1.status[0])    
################## ThaiSmileAir Bangkok to Chiang Mai##########################
i = "01:20"
# Time Revival
ThaiSmileAir_flight_ids = {
    "07:25": "WE102", "09:00": "WE108", "10:20": "WE104", "13:30": "WE110", "15:05": "WE164", "19:15": "WE120"
}

departure_ThaiSmileAir_BKK_to_CNX = {
    'Monday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Tuesday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Wednesday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Thursday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Friday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Saturday': ["07:25","09:00","10:20","13:30","15:05","19:15"],
    'Sunday': ["07:25","09:00","10:20","13:30","15:05","19:15"]
}


arrival_ThaiSmileAir_BKK_to_CNX = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Sunday']]
}

for element_details1.day , departure_list in departure_ThaiSmileAir_BKK_to_CNX.items():
    arrival_list = arrival_ThaiSmileAir_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Smile_Air = ThaiSmileAir_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[2].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Smile_Air, element_details1.status[0])
################## AirAsia Bangkok to Chiang Mai##########################
i = "01:10"
# Time Revival
airasia_flight_ids = {
    "06:45": "FD4100", "11:25": "FD4104",  "15:50": "FD4106"
}

departure_AirAsia_BKK_to_CNX = {
    'Monday': ["06:45", "15:50"],
    'Tuesday': ["06:45", "11:25","15:50"],
    'Wednesday': ["06:45"],
    'Thursday': ["11:25","15:50"],
    'Friday': ["11:25","15:50"],
    'Saturday': ["11:25","15:50"],
    'Sunday': ["11:25","15:50"]
}

arrival_AirAsia_BKK_to_CNX = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Sunday']]
}

for element_details1.day , departure_list in departure_AirAsia_BKK_to_CNX.items():
    arrival_list = arrival_AirAsia_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_AirAsia = airasia_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[3].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_AirAsia, element_details1.status[0])
################## Vietjet Bangkok to HKT Phuket ##########################
vietjet_flight_ids = {
    "07:00": "VZ314",  "08:00": "VZ317",  "08:10": "VZ300",  "08:55": "VZ315",  "10:45": "VZ300",  "10:50": "VZ304", "12:45": "VZ305", "12:55": "VZ310",
    "13:00": "VZ2303", "13:15": "VZ310",  "13:50": "VZ2300", "14:40": "VZ302", "15:35": "VZ306",  "15:55": "VZ2301", "16:35": "VZ308", "18:15": "VZ2304", "18:30": "VZ309", "20:15": "VZ2305", "20:30" : "VZ312", "21:35": "VZ316"
}

departure_VietJet_BKK_to_HKT = {
    'Monday': ["07:00", "10:50", "13:15", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Tuesday': ["07:00", "10:45", "10:50", "12:55", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Wednesday': ["07:00", "10:50", "13:15", "13:50", "14:40", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Thursday': ["07:00", "10:50", "12:55", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Friday': ["07:00", "10:50", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Saturday': ["07:00", "10:50", "12:55", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"],
    'Sunday': ["07:00", "10:50", "13:50", "15:35", "16:35", "18:15", "20:30", "21:35"]
}

i = "01:25"

arrival_VietJet_BKK_to_HKT = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HKT['Sunday']]
}


for element_details1.day , departure_list in departure_VietJet_BKK_to_HKT.items():
    arrival_list = arrival_VietJet_BKK_to_HKT[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[4], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_Vietjet, element_details1.status[0])
                
################## BangkokAir Bangkok to HKT Phuket##########################
i = "01:20"
# Time Revival
bangkok_flight_ids = {
    "08:05": "PG271", "10:50": "PG275", "12:35": "PG273", "16:55": "PG277", "19:45": "PG279"
}

departure_Bangkok_BKK_to_HKT = {
    'Monday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Tuesday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Wednesday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Thursday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Friday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Saturday': ["08:05", "10:50", "12:35", "16:55", "19:45"],
    'Sunday': ["08:05", "10:50", "16:55", "19:45"]
}

arrival_Bangkok_BKK_to_HKT = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_Bangkok_BKK_to_HKT['Sunday']]
}

for element_details1.day , departure_list in departure_Bangkok_BKK_to_HKT.items():
    arrival_list = arrival_Bangkok_BKK_to_HKT[element_details1.day]
    for i in range(len(departure_list)):
        id_Bangkok = bangkok_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[1].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[4], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Bangkok, element_details1.status[0])    
################## ThaiSmileAir Bangkok to HKT Phuket##########################
i = "01:20"
# Time Revival
ThaiSmileAir_flight_ids = {
    "07:30": "WE289", "08:05": "WE201", "09:30": "WE285", "10:50": "WE203", "12:00": "WE8783", "13:55": "WE215", "14:55": "WE110", "17:30": "WE217", "19:10": "WE211"
}

departure_ThaiSmileAir_BKK_to_HKT = {
    'Monday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"],
    'Tuesday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"],
    'Wednesday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"],
    'Thursday': ["07:30", "08:05", "09:30", "10:50","12:00", "13:55", "14:55", "17:30", "19:10"],
    'Friday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"],
    'Saturday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"],
    'Sunday': ["07:30", "08:05", "09:30", "10:50", "13:55", "14:55", "17:30", "19:10"]
}


arrival_ThaiSmileAir_BKK_to_HKT = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_HKT['Sunday']]
}

for element_details1.day , departure_list in departure_ThaiSmileAir_BKK_to_HKT.items():
    arrival_list = arrival_ThaiSmileAir_BKK_to_HKT[element_details1.day]
    for i in range(len(departure_list)):
        id_Smile_Air = ThaiSmileAir_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[2].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[4], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Smile_Air, element_details1.status[0])
################## AirAsia Bangkok to HKT Phuket##########################
i = "01:10"
# Time Revival
airasia_flight_ids = {
    "06:35": "FD4112", "10:15": "FD4110",  "20:35": "FD4124"
}

departure_AirAsia_BKK_to_HKT = {
    'Monday': ["06:35", "10:15", "20:35"],
    'Tuesday': ["06:35", "10:15", "20:35"],
    'Wednesday': ["06:35", "10:15", "20:35"],
    'Thursday': ["06:35", "10:15", "20:35"],
    'Friday': ["06:35", "10:15", "20:35"],
    'Saturday': ["06:35", "10:15", "20:35"],
    'Sunday': ["06:35", "10:15", "20:35"]
}

arrival_AirAsia_BKK_to_HKT = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_AirAsia_BKK_to_HKT['Sunday']]
}

for element_details1.day , departure_list in departure_AirAsia_BKK_to_HKT.items():
    arrival_list = arrival_AirAsia_BKK_to_HKT[element_details1.day]
    for i in range(len(departure_list)):
        id_AirAsia = airasia_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[3].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[4], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_AirAsia, element_details1.status[0])
################## Vietjet Bangkok to HDY HadYai ##########################
vietjet_flight_ids = {
    "07:10": "VZ320",  "11:15": "VZ324", "17:00": "VZ326",  "19:55" : "VZ328"
}

departure_VietJet_BKK_to_HDY = {
    'Monday': ["07:10", "11:15", "17:00", "19:55"],
    'Tuesday': ["07:10", "11:15", "17:00", "19:55"],
    'Wednesday': ["07:10", "11:15", "17:00", "19:55"],
    'Thursday': ["07:10", "11:15", "17:00", "19:55"],
    'Friday': ["07:10", "11:15", "17:00", "19:55"],
    'Saturday': ["07:10", "11:15", "17:00", "19:55"],
    'Sunday': ["07:10", "11:15", "17:00", "19:55"]
}

i = "01:25"

arrival_VietJet_BKK_to_HDY = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_HDY['Sunday']]
}


for element_details1.day , departure_list in departure_VietJet_BKK_to_HDY.items():
    arrival_list = arrival_VietJet_BKK_to_HDY[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[5], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_Vietjet, element_details1.status[0])
                 
################## ThaiSmileAir Bangkok to HDY HadYai ##########################
# Time Revival 1.30 - 1.25
ThaiSmileAir_flight_ids = {
    "07:00": "WE259", "12:30": "WE267", "18:30": "WE263"
}

departure_ThaiSmileAir_BKK_to_HDY = {
    'Monday': ["07:00", "12:30", "18:30"],
    'Tuesday': ["07:00", "12:30", "18:30"],
    'Wednesday': ["07:00", "12:30", "18:30"],
    'Thursday': ["07:00", "12:30", "18:30"],
    'Friday': ["07:00", "12:30", "18:30"],
    'Saturday': ["07:00", "12:30", "18:30"],
    'Sunday': ["07:00", "12:30", "18:30"]
}


arrival_ThaiSmileAir_BKK_to_HDY = {
    'Monday': ["08:25", "14:00", "20:00"],
    'Tuesday': ["08:25", "14:00", "20:00"],
    'Wednesday': ["08:25", "14:00", "20:00"],
    'Thursday': ["08:25", "14:00", "20:00"],
    'Friday': ["08:25", "14:00", "20:00"],
    'Saturday': ["08:25", "14:00", "20:00"],
    'Sunday': ["08:25", "14:00", "20:00"]
}

for element_details1.day , departure_list in departure_ThaiSmileAir_BKK_to_HDY.items():
    arrival_list = arrival_ThaiSmileAir_BKK_to_HDY[element_details1.day]
    for i in range(len(departure_list)):
        id_Smile_Air = ThaiSmileAir_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[2].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[5], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Smile_Air, element_details1.status[0])
        
################## Vietjet Bangkok to UTH Udon ##########################
vietjet_flight_ids = {
    "08:30": "VZ200",  "13:30": "VZ204",  "15:30": "VZ202"
}

departure_VietJet_BKK_to_UTH = {
    'Monday': ["08:30", "13:30", "15:30"],
    'Tuesday': ["08:30", "13:30", "15:30"],
    'Wednesday': ["08:30", "13:30", "15:30"],
    'Thursday': ["08:30", "13:30", "15:30"],
    'Friday': ["08:30", "13:30", "15:30"],
    'Saturday': ["08:30", "13:30", "15:30"],
    'Sunday': ["08:30", "13:30", "15:30"]
}

i = "01:10"

arrival_VietJet_BKK_to_UTH = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_VietJet_BKK_to_UTH['Sunday']]
}


for element_details1.day , departure_list in departure_VietJet_BKK_to_UTH.items():
    arrival_list = arrival_VietJet_BKK_to_UTH[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[6], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, element_details1.reschedule, id_Vietjet, element_details1.status[0])

################## ThaiSmileAir Bangkok to UTH Udon ##########################
i = "01:10"
# Time Revival
ThaiSmileAir_flight_ids = {
    "07:00": "WE2", "12:15": "WE4", "14:35": "WE6", "17:55": "WE8"
}

departure_ThaiSmileAir_BKK_to_UTH = {
    'Monday': ["07:00", "12:15", "14:35", "17:55"],
    'Tuesday': ["07:00", "12:15", "14:35", "17:55"],
    'Wednesday': ["07:00", "12:15", "14:35", "17:55"],
    'Thursday': ["07:00", "12:15", "14:35", "17:55"],
    'Friday': ["07:00", "12:15", "14:35", "17:55"],
    'Saturday': ["07:00", "12:15", "14:35", "17:55"],
    'Sunday': ["07:00", "12:15", "14:35", "17:55"]
}


arrival_ThaiSmileAir_BKK_to_UTH = {
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) if int(time[3:])+int(i[3:]) < 60 else str((int(time[:2])+int(i[:2])+60//60)%24).zfill(2)+":"+str((int(time[3:])+int(i[3:]))%60).zfill(2) for time in departure_ThaiSmileAir_BKK_to_UTH['Sunday']]
}

for element_details1.day , departure_list in departure_ThaiSmileAir_BKK_to_UTH.items():
    arrival_list = arrival_ThaiSmileAir_BKK_to_UTH[element_details1.day]
    for i in range(len(departure_list)):
        id_Smile_Air = ThaiSmileAir_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[2].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[6], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, element_details1.reschedule, id_Smile_Air, element_details1.status[0])
###################################################################################################################################################################################################################################################################################
my_trip = Trip()

#test trip
depart,arrival,travelday = input().split("/")
print(my_trip.search_flight(depart,arrival,travelday))

#test airline
# airline,day = input().split("/")
# print(my_trip.search_airline(airline,day))

