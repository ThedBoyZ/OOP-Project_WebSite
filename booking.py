from datetime import date, datetime
import time
from account import Traveler, Contact
from total_price import PriceDetailCollection
from flights import Trip


class BookingSystem:
    def __init__(self):
        self.__airpaz_code = None
        self.__booking_date = None
        self.__trip = None
        self.__travelers = []
        self.__number_of_travelers = len(self.__travelers) + 1
        self.__contact_info = None
        self.__price_details = None
        self.__status = "In Progress"      # In Progress, Need Payment

    @staticmethod
    def generate_airpaz_code():
        timestamp = int(time.time())
        return timestamp

    @staticmethod
    def calculate_price(trip, travelers):
        price_collection = PriceDetailCollection(trip, travelers)
        return price_collection.get_price_details()
    
    @property
    def airpaz_code(self):
        return self.__airpaz_code
    
    @property
    def travelers(self):
        return self.__travelers
    
    @travelers.setter
    def travelers(self, travelers):
        self.__travelers = travelers
    
    @property
    def booking_date(self):
        return self.__booking_date
    
    @property
    def total_price(self):
        return self.__total_price
    
    @total_price.setter
    def total_price(self, total_price):
        self.__total_price = total_price
    
    def add_ons_baggage(self, index, baggage_weight: int=0):
        self.__travelers[index]['baggage_weight'] += baggage_weight
        return self.__travelers

    def booking(self, trip, contact, travelers):
        # Set trip, contact info, and traveler info
        self.__trip = trip
        self.__contact_info = contact
        
        for traveler in travelers:
            # Check if the traveler already exists in the booking
            if traveler not in self.__travelers:
                self.__travelers.append(traveler)

        # Generate booking ID and calculate total price
        self.__airpaz_code = str(self.generate_airpaz_code())
        self.__booking_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__price_details = self.calculate_price(self.__trip, self.__travelers)

        # Set initial status as "Need Payment"
        self.__status = "Need Payment"

        # Return the booking ID
        return self.airpaz_code
    
    def get_booking_by_id(self, id):
        if id == self.airpaz_code:

            traveler_details = []
            for traveler in self.__travelers:
                traveler_details.append(traveler.get_traveler_info())

            return {
                "airpaz_code": self.airpaz_code,
                "booking_date": self.booking_date,
                "trip_detail": self.__trip,
                "contact_info": self.__contact_info.get_contact_info(),
                "number_of_travelers": self.__number_of_travelers,
                "travelers": traveler_details,
                "price_details": self.__price_details,
                "status": self.__status
            }
        else:
            raise ValueError("Invalid airpaz code.")
        
    def __str__(self):
        traveler_details = []
        for traveler in self.__travelers:
            traveler_details.append(traveler.get_traveler_info())

        return {
            "airpaz_code": self.airpaz_code,
            "booking_date": self.booking_date,
            "trip_detail": self.__trip,
            "contact_info": self.__contact_info.get_contact_info(),
            "travelers": traveler_details,
            "price_details": self.__price_details,
            "status": self.__status
        }

if __name__ == "__main__":
    
    # selected flight
    trip1 = Trip()
    my_trip = trip1.search_flight('BKK', 'CNX', 'Monday')

    contact = Contact("Tanathip", "Pona", "Mr.", "petch@gmail.com", "0800687960")

    t1 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand")
    t2 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand")
    travelers = []
    travelers.append(t1)
    travelers.append(t2)

    # booking
    booking1 = BookingSystem()
    print(booking1.booking(my_trip, contact, travelers))