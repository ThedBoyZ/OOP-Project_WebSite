from datetime import date
from account import Traveler


# Define a class to hold price details for a single passenger
class PriceDetail:
    def __init__(self, type_person, baggage_weight):
        self._init_person_price(type_person)
        self._init_baggage_price(baggage_weight)

    def _init_person_price(self, person_type: str):
        # Initialize person price based on type
        if person_type.upper() == "ADULT":
            self.person_price = 803
        elif person_type.upper() == "CHILD":
            self.person_price = 803
        elif person_type.upper() == "INFANT":
            self.person_price = 300
        else:
            raise ValueError("Invalid person type.")

    def _init_baggage_price(self, baggage_weight):
        # Initialize baggage price based on weight
        if str(baggage_weight) in ["15", "20", "25", "30", "35", "40"]:
            self.baggage_price = [
                418,    # 15 kg
                465,    # 20 kg
                583,    # 25 kg
                936,    # 30 kg
                1125,   # 35 kg
                1407    # 40 kg
            ][(int(baggage_weight) // 5) - 3]
        elif str(baggage_weight) == "0":
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


if __name__ == '__main__':

    t1 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand")
    t2 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand")
    t3 = Traveler("Infant", "", "Male", "Angry", "Bird", date(2023, 3, 27), "Thailand")

    details = PriceDetailCollection()
    details.add_price_detail(t1)
    details.add_price_detail(t2)
    details.add_price_detail(t3)

    print("Total price:", details.total_price(), "bath")