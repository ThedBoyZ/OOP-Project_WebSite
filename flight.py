from add_airline import AirlineCollection
from add_airport import AirportCollection
from datetime import datetime


class Flight:

    airline_coll = AirlineCollection()
    airport_coll = AirportCollection()

    def __init__(self, flight_id, departure_airport, arrival_airport, day, departure_datetime, arrival_datetime, airline_name, cabin_baggage=0, refund=False, reschedule=False, status="On Time"):
        self.flight_id = flight_id
        self.cabin_baggage = cabin_baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport = Flight.airport_coll.airports[departure_airport].name
        self.arrival_airport = Flight.airport_coll.airports[arrival_airport].name
        self.day = day
        self.airline_name = Flight.airline_coll.airlines[airline_name].name
        self.airline_logo = Flight.airline_coll.airlines[airline_name].logo

        self.departure_datetime = datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M")
        self.departure_year = self.departure_datetime.strftime("%Y")
        self.departure_month = self.get_month(self.departure_datetime)
        self.departure_day = self.departure_datetime.strftime("%d")
        self.departure_time = self.departure_datetime.strftime("%H:%M")

        self.arrival_datetime = datetime.strptime(arrival_datetime, "%Y-%m-%d %H:%M")
        self.arrival_year = self.arrival_datetime.strftime("%Y")
        self.arrival_month = self.get_month(self.arrival_datetime)
        self.arrival_day = self.arrival_datetime.strftime("%d")
        self.arrival_time = self.arrival_datetime.strftime("%H:%M")

    
    def __str__(self):
        return "Airline: {!r} \nFlight ID: {} \nFrom {!r} ({}) to {!r} ({})".format(self.airline_name, self.flight_id, self.departure_airport, self.departure_datetime, self.arrival_airport, self.arrival_datetime)
    
    @staticmethod
    def get_month(datetime):
        if datetime.strftime("%m") in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            return [
                "January",      # 01
                "February",     # 02
                "March",        # 03
                "April",        # 04
                "May",          # 05
                "June",         # 06
                "July",         # 07
                "August",       # 08
                "September",    # 09
                "October",      # 10
                "November",     # 11
                "December"      # 12
            ][int(datetime.strftime("%m")) - 1]
        else:
            raise ValueError("Invalid month.")
    

class Trip:
    def __init__(self):
        self.__flights = {}
        self.__transit = count_transit

    def add_flight(self, flight):
        if flight.flight_id in self.__flights.values():
            raise ValueError("Flight already exist")
        self.__flights[flight_id] = flight

    def __str__(self):
        output = "List of Trip:\n"
        for flight in self.flights:
            output += f"{flight}\n"
            output += "-"*40
            output += "\n"
        output += f"{self.count_transit} transit"
        return output


if __name__ == "__main__":
    
    flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 12:30", "Thai Vietjet Air")
    flight2 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)
    
    trip1 = Trip([flight1, flight2], count_transit=1)
    print(trip1)