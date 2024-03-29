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
class Trip(list):
    
    def search_airline(self, airline_name, day):
        matching_flights = []
        for flight in Flight.all_flight:
            if airline_name == flight[0]:
              if day == flight[1]:
                matching_flights.append(flight)
                print(flight)
        print("\n")
        return matching_flights

    
class Flight:
   
    all_flight = Trip() #only select Trip
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
        

class Element_Details_Flight:
    def __init__(self, day, departure_airport, arrival_airport, id_Vietjet, id_AirAsia, id_Smile_Air, id_Bangkok, baggage, refund, status):
        self.day = day
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.id_Vietjet = id_Vietjet
        self.id_AirAsia = id_AirAsia
        self.id_Smile_Air = id_Smile_Air
        self.id_Bangkok = id_Bangkok
        self.baggage = baggage
        self.refund = refund
        self.status = status

element_details1 = Element_Details_Flight(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ["BKK","DMK","PHS","CNX","HKT","HDY","UTH","CEI","KKC","KBV","UBP","NST","URT","KOP"],
    ["BKK","DMK","PHS","CNX","HKT","HDY","UTH","CEI","KKC","KBV","UBP","NST","URT","KOP"],
    ["VZ100","VZ102","VZ104","VZ106","VZ110","VZ114","VZ2104","VZ2106","VZ2114","VZ118","VZ120","VZ122","VZ300","VZ305","VZ306","VZ308","VZ310","VZ312","VZ314","VZ315","VZ316","VZ317","VZ2300","VZ2304"],
    ["FD4100","FD4104","FD4106"],
    ["WE102","WE104","WE108","WE110","WE120","WE164"],
    ["PG215","PG217","PG219","PG223"],
    [7,20],
    False,
    ["One Way","Round Trip"]
)
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
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_CNX['Sunday']]
}

flights = []
for element_details1.day , departure_list in departure_VietJet_BKK_to_CNX.items():
    arrival_list = arrival_VietJet_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, id_Vietjet, element_details1.status[0])
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
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_Bangkok_BKK_to_CNX['Sunday']]
}
flights = []
for element_details1.day , departure_list in departure_Bangkok_BKK_to_CNX.items():
    arrival_list = arrival_Bangkok_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Bangkok = bangkok_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[1].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[1], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, id_Bangkok, element_details1.status[0])    
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
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_ThaiSmileAir_BKK_to_CNX['Sunday']]
}

flights = []
for element_details1.day , departure_list in departure_ThaiSmileAir_BKK_to_CNX.items():
    arrival_list = arrival_ThaiSmileAir_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_Smile_Air = ThaiSmileAir_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[2].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[2], None, arrival_list[i], element_details1.baggage[1], element_details1.refund, id_Smile_Air, element_details1.status[0])
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
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_AirAsia_BKK_to_CNX['Sunday']]
}
flights = []
for element_details1.day , departure_list in departure_AirAsia_BKK_to_CNX.items():
    arrival_list = arrival_AirAsia_BKK_to_CNX[element_details1.day]
    for i in range(len(departure_list)):
        id_AirAsia = airasia_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[3].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[3], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, id_AirAsia, element_details1.status[0])
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
    'Monday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Monday']],
    'Tuesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Tuesday']],
    'Wednesday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Wednesday']],
    'Thursday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Thursday']],
    'Friday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Friday']],
    'Saturday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Saturday']],
    'Sunday': [str(int(time[:2])+int(i[:2])).zfill(2)+":"+str(int(time[3:])+int(i[3:])).zfill(2) for time in departure_VietJet_BKK_to_HKT['Sunday']]
}
flights = []
for element_details1.day , departure_list in departure_VietJet_BKK_to_HKT.items():
    arrival_list = arrival_VietJet_BKK_to_HKT[element_details1.day]
    for i in range(len(departure_list)):
        id_Vietjet = vietjet_flight_ids[departure_list[i]]
        flight = Flight(airline_coll.airlines[0].name, element_details1.day, element_details1.departure_airport[0], None, departure_list[i],\
                        element_details1.arrival_airport[4], None, arrival_list[i], element_details1.baggage[0], element_details1.refund, id_Vietjet, element_details1.status[0])
                
#######################################################################################################################################################################################
my_trip = Trip()
search,travelday = input().split("/")
#my_trip.search_flight("air asia")
print(my_trip.search_airline(search,travelday))
#print(Flight.all_flight)

#print(Flight1.name)
#print(Trip().search_flight("air asia"))
# bkk_to_cnx = Flight('000001', 7, False, False, True, 'BKK', 'Sunday', '15:00', 'CNX', 'Sunday', '17:10', 'Thai Vietjet Air')
# cnx_to_bkk = Flight('000002', 7, False, False, True, 'CNX', 'Monday', '10:00', 'BKK', 'Monday', '11:30', 'Thai Vietjet Air')


#print(Flight1.name)