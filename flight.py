from add_airline import AirlineCollection
from add_airport import AirportCollection
from datetime import datetime


class Flight:

    airline_coll = AirlineCollection()
    airport_coll = AirportCollection()

    def __init__(self, flight_id, departure_airport, arrival_airport, day, departure_datetime, arrival_datetime, airline_name, cabin_baggage=0, refund=False, reschedule=False, status="On Time"):
        self.__flight_id = flight_id
        self.__cabin_baggage = cabin_baggage
        self.__refund = refund
        self.__reschedule = reschedule
        self.__status = status
        self.__departure_airport = Flight.airport_coll.airports[departure_airport].name
        self.__arrival_airport = Flight.airport_coll.airports[arrival_airport].name
        self.__day = day
        self.__airline_name = Flight.airline_coll.airlines[airline_name].name

        self.__departure_datetime = datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M")
        self.__departure_date = self.__departure_datetime.strftime("%Y-%m-%d")
        self.__departure_time = self.__departure_datetime.strftime("%H:%M")

        self.__arrival_datetime = datetime.strptime(arrival_datetime, "%Y-%m-%d %H:%M")
        self.__arrival_date = self.__arrival_datetime.strftime("%Y-%m-%d")
        self.__arrival_time = self.__arrival_datetime.strftime("%H:%M")

    @property
    def flight_id(self):
        return self.__flight_id
    
    def get_flight_detail(self):
        return {
            "flight_id": self.__flight_id,
            "airline_name": self.__airline_name,
            "day": self.__day,
            "departure_date": self.__departure_date,
            "departure_time": self.__departure_time,
            "arrival_date": self.__arrival_date,
            "arrival_time": self.__arrival_time,
            "departure_airport": self.__departure_airport,
            "arrival_airport": self.__arrival_airport,
            "cabin_baggage": self.__cabin_baggage,
            "refund": self.__refund,
            "reschedule": self.__reschedule,
            "status": self.__status
        }
    

class Trip:
    def __init__(self):
        self.__flights = []
        self.__count_flight = 0
        self.__transit = 0

    def add_flight(self, flight):
        if flight in self.__flights:
            raise ValueError("Flight already exist")
        self.__flights.append(flight.get_flight_detail())
        self.__count_flight += 1
        self.__transit = self.__count_flight - 1
    
    @property
    def flights(self):
        return self.__flights
    
    @property
    def transit(self):
        return self.__transit
    
    def get_trip_detail(self):
        return {
            "transit": self.transit,
            "flight_detail": self.flights
        }

if __name__ == "__main__":
    
    flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 12:30", "Thai Vietjet Air")
    flight2 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)
    
    trip1 = Trip()
    trip1.add_flight(flight1)
    trip1.add_flight(flight2)