import re
from dataclasses import dataclass
from datetime import date
from account import Traveler


# Define a class to hold price details for a single passenger
class PriceDetail:
    def __init__(self, person_type: str, baggage_weight: str):
        self._init_person_price(person_type)
        self._init_baggage_price(baggage_weight)

    def _init_person_price(self, person_type: str):
        # Initialize person price based on type
        if person_type.lower() == "adult":
            self.person_price = 803
        elif person_type.lower() == "child":
            self.person_price = 803
        elif person_type.lower() == "infant":
            self.person_price = 300
        else:
            raise ValueError("Invalid person type.")

    def _init_baggage_price(self, baggage_weight: str):
        # Initialize baggage price based on weight
        if baggage_weight in ["15", "20", "25", "30", "35", "40"]:
            self.baggage_price = [
                418,    # 15 kg
                465,    # 20 kg
                583,    # 25 kg
                936,    # 30 kg
                1125,   # 35 kg
                1407    # 40 kg
            ][(int(baggage_weight) // 5) - 3]
        elif baggage_weight == "0":
            self.baggage_price = 0
        else:
            raise ValueError("Invalid baggage weight.")

    def total_price(self) -> int:
        # Return the sum of the person and baggage prices
        return self.person_price + self.baggage_price


# Define a class to hold a collection of price details for multiple passengers
class PriceDetailCollection:
    def __init__(self):
        self.details = []

    def add_price_detail(self, traveler: Traveler):
        detail = PriceDetail(traveler.type_person, traveler.baggage_weight)
        self.details.append(detail)

    def total_price(self) -> int:
        # Return the sum of the total prices for all price details in the collection
        return sum(detail.total_price() for detail in self.details)


class TravelerPrice:
    def __init__(self, adult_price, child_price, infant_price):
        self.adult_price = adult_price
        self.child_price = child_price
        self.infant_price = infant_price

class BaggagePrice:
    def __init__(self, baggage_weight, baggage_price):
        self.baggage_weight = baggage_weight
        self.baggage_price = baggage_price
        self.__details = []

    @property
    def details(self):
        return self.__details
    
    def add_baggage_detail(self):
        self.details.append(self.baggage_weight, self.baggage_price)


if __name__ == '__main__':

    # t1 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand", "15")
    # t2 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand", "20")
    # t3 = Traveler("Infant", "", "Male", "Angry", "Bird", date(2023, 3, 27), "Thailand", "0")

    # details = PriceDetailCollection()
    # details.add_price_detail(t1)
    # details.add_price_detail(t2)
    # details.add_price_detail(t3)

    # print("Total price:", details.total_price(), "bath")

    BaggagePrice("10kg", 480)