from airport_and_airline import AirlineCollection, AirportCollection, Image
from datetime import datetime

airport_coll = AirportCollection()
airport_coll.add_airport("Suvarnabhumi Airport", "BKK", "")
airport_coll.add_airport("Don Mueang International Airport", "DMK", "Terminal 2")
airport_coll.add_airport("Chiang Mai International Airport", "CNX", "Terminal Domestic")

airline_coll = AirlineCollection()
airline_coll.add_airline("Thai Vietjet Air" , Image('images/airlines/thai_vietjet_air.png'))
airline_coll.add_airline("Bangkok Airways"  , Image('images/airlines/bangkok_airways.png'))
airline_coll.add_airline("Thai Smile Air"   , Image('images/airlines/thai_smile_air.png'))
airline_coll.add_airline("Thai AirAsia"     , Image('images/airlines/thai_airasia.png'))
airline_coll.add_airline("Nok Air"          , Image('images/airlines/nok_air.png'))

class Flight:
    def __init__(self, flight_id, departure_airport_code, arrival_airport_code, day, departure_datetime, arrival_datetime, airline_name, cabin_baggage=0, refund=False, reschedule=False, status="On Time"):
        self.flight_id = flight_id
        self.cabin_baggage = cabin_baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport_code = departure_airport_code
        self.arrival_airport_code = arrival_airport_code
        self.day = day
        self.airline_name = airline_name
        self.airline_image = airline_coll.get_airline_image(airline_name)
        self.departure_airport = airport_coll.get_airport_name(departure_airport_code)
        self.arrival_airport = airport_coll.get_airport_name(arrival_airport_code)

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
        return "{!r} Flight {}: {!r} to {!r}".format(self.airline_name, self.flight_id, self.departure_airport, self.arrival_airport)
    
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
    def __init__(self, flights, count_transit=0):
        self.flights = flights
        self.count_transit = count_transit

    def __str__(self):
        output = "List of Trip:\n"
        for flight in self.flights:
            output += "{}\n".format(flight)
        output += "{} transit".format(self.count_transit)
        return output


if __name__ == "__main__":
    
    flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 18:00", "Thai Vietjet Air")
    # print(flight1.departure_year)
    # print(flight1.departure_month)
    # print(flight1.departure_day)
    # print(flight1.departure_time)
    # print(flight1)
    flight2 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)
    # print(flight2)
    # print(flight2.reschedule)
    

    trip1 = Trip([flight1, flight2], count_transit=1)
    print(trip1)