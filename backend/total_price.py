from datetime import date
from account import Traveler
from flight import Trip
from Coupon import coupon_list


# Define a class to hold price details for a single passenger
class PriceDetail:

    DISTANCE_INDEX_MAP = {
        ("BKK", "HDY"): 5,
        ("HDY", "BKK"): 5,
        ("BKK", "HKT"): 4,
        ("HKT", "BKK"): 4,
        ("BKK", "CNX"): 3,
        ("CNX", "BKK"): 3,
        ("BKK", "UBP"): 2,
        ("UBP", "BKK"): 2,
        ("BKK", "UTH"): 1,
        ("UTH", "BKK"): 1,
    }

    def __init__(self, day, departure, arrival, airline_name, person_type, baggage_weight):
        self.day = day
        self.departure = departure
        self.arrival = arrival
        self.airline_name = airline_name
        self.person_type = person_type
        self.distance_index = self.calculate_distance_index()
        self.baggage_weight = baggage_weight

    def calculate_distance_index(self) -> int:
        key = (self.departure, self.arrival)
        if key in PriceDetail.DISTANCE_INDEX_MAP:
            return PriceDetail.DISTANCE_INDEX_MAP[key]
        else:
            raise ValueError(f"Invalid departure/arrival airports: {self.departure}/{self.arrival}")

    def calculate_person_price(self) -> float:
        if self.airline_name == "Thai Vietjet Air":
            if self.day in ["Saturday", "Sunday"]:
                base_price = 1200
            else:
                base_price = 900
            price_per_distance = 49
        elif self.airline_name == "Bangkok Airways":
            if self.day in ["Saturday", "Sunday"]:
                base_price = 1200
            else:
                base_price = 900
            price_per_distance = 52
        elif self.airline_name == "Thai Smile Air":
            if self.day in ["Saturday", "Sunday"]:
                base_price = 1200
            else:
                base_price = 900
            price_per_distance = 54
        elif self.airline_name == "Thai AirAsia":
            if self.day in ["Saturday", "Sunday"]:
                base_price = 1200
            else:
                base_price = 900
            price_per_distance = 56
        else:
            raise ValueError("Invalid airline name.")

        if self.person_type.upper() == "ADULT":
            person_price = base_price + (self.distance_index * price_per_distance)
        elif self.person_type.upper() == "CHILD":
            person_price = base_price + (self.distance_index * price_per_distance)
        elif self.person_type.upper() == "INFANT":
            person_price = 300
        else:
            raise ValueError("Invalid person type.")

        return person_price

    def calculate_baggage_price(self):
        # Initialize baggage price based on weight
        if str(self.baggage_weight) in ["15", "20", "25", "30", "35", "40"]:
            baggage_price = [
                418,    # 15 kg
                465,    # 20 kg
                583,    # 25 kg
                936,    # 30 kg
                1125,   # 35 kg
                1407    # 40 kg
            ][(int(self.baggage_weight) // 5) - 3]
        elif str(self.baggage_weight) == "0":
            baggage_price = 0
        else:
            raise ValueError("Invalid baggage weight.")
        
        return baggage_price

    def total_price(self) -> int:
        # Return the sum of the person and baggage prices
        return self.calculate_person_price() + self.calculate_baggage_price()


# Define a class to hold a collection of price details for multiple passengers
class PriceDetailCollection:
    def __init__(self, trip):
        self.number_of_adult = 0
        self.number_of_child = 0
        self.number_of_infant = 0
        self.__trip = trip
        self.__details = []

    def add_price_detail(self, traveler: Traveler):
        detail = PriceDetail(self.__trip["day"], self.__trip["departure_airport"], self.__trip["arrival_airport"], self.__trip["airline_name"], traveler.type_person, traveler.baggage_weight)
        self.__details.append(detail)
        if detail.person_type == "Adult":
            self.number_of_adult += 1
        elif detail.person_type == "Child":
            self.number_of_child += 1
        elif detail.person_type == "Infant":
            self.number_of_infant += 1

    def discount(self, promo_code = '0'):
        for coupon in coupon_list._coupon_detail:
            if promo_code == coupon.code:
                return self.total_price() * (100 - coupon.discount) / 100

    def total_baggage_price(self) -> int:
        return sum(detail.calculate_baggage_price() for detail in self.__details)

    def total_price(self) -> int:
        # Return the sum of the total prices for all price details in the collection
        return sum(detail.total_price() for detail in self.__details)

    def get_price_details(self):
        output = {}

        for detail in self.__details:
            price_detail = detail
            if price_detail.person_type == "Adult":
                output["Adult"] = {
                    "Number_of_Adult": self.number_of_adult,
                    "Total": price_detail.calculate_person_price()
                }
            if price_detail.person_type == "Child":
                output["Child"] = {
                    "Number_of_Child": self.number_of_child,
                    "Total": price_detail.calculate_person_price()
                }
            if price_detail.person_type == "Infant":
                output["Infant"] = {
                    "Number_of_Infant": self.number_of_infant,
                    "Total": price_detail.calculate_person_price()
                }
        
        output["Baggage_price"] = self.total_baggage_price()
        output["Total_price"] = self.total_price()
        return output

if __name__ == '__main__':

    t1 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand")
    t2 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand", "15")
    t3 = Traveler("Infant", "", "Male", "Angry", "Bird", date(2023, 3, 27), "Thailand")

    trip1 = Trip()
    my_trip = trip1.search_flight('BKK', 'CNX', 'Friday')

    details = PriceDetailCollection(my_trip[2])
    details.add_price_detail(t1)
    details.add_price_detail(t2)
    details.add_price_detail(t3)

    # print("Total price:", details.total_price(), "bath")
    # print(details.get_price_details())
    print(details.discount("dc10"))