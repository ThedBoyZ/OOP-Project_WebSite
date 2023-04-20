from datetime import date, datetime
import time
from account import Traveler, Contact
from total_price import PriceDetailCollection
from flight import Flight, Trip


class BookingSystem:
    def __init__(self):
        self.__booking_id = None
        self.__booking_date = None
        self.__trip = None
        self.__travelers = []
        self.__contact_info = None
        self.__total_price = 0
        self.__status = "In Progress"      # In Progress, Need Payment

    @staticmethod
    def generate_booking_id():
        timestamp = int(time.time())
        return f"BK{timestamp}"

    @staticmethod
    def calculate_total_price(travelers):
        price_collection = PriceDetailCollection()
        for traveler in travelers:
            price_collection.add_price_detail(traveler)
        return price_collection.total_price()
    
    @property
    def booking_id(self):
        return self.__booking_id
    
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
    
    def add_ons_baggage(self, index, baggage_weight):
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
        self.__booking_id = self.generate_booking_id()
        self.__booking_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__total_price = self.calculate_total_price(self.__travelers)

        # Set initial status as "Need Payment"
        self.__status = "Need Payment"

        # Return the booking ID
        return self.booking_id
    
    def get_booking_by_id(self, id):
        if id == self.booking_id:

            traveler_details = []
            for traveler in self.__travelers:
                traveler_details.append(traveler.get_traveler_info())

            return {
                "booking_id": self.booking_id,
                "booking_date": self.booking_date,
                "trip_detail": self.__trip,
                "contact_info": self.__contact_info.get_contact_info(),
                "travelers": traveler_details,
                "total_price": self.total_price,
                "status": self.__status
            }
        else:
            raise ValueError("Invalid booking ID.")
        
    def __str__(self):
        return {
                "booking_id": self.booking_id,
                "booking_date": self.booking_date,
                "trip_detail": self.__trip,
                "contact_info": self.__contact_info,
                "travelers": self.travelers,
                "total_price": self.__total_price,
                "status": self.__status
            }

if __name__ == "__main__":
    
    # flight
    flight1 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)
    flight2 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 12:30", "Thai Vietjet Air")

    # trip
    trip1 = Trip()
    trip1.add_flight(flight1)
    # trip1.add_flight(flight2)

    contact = Contact("Tanathip", "Pona", "Mr.", "petch@gmail.com", "0800687960")

    t1 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand")
    t2 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand")
    travelers = []
    travelers.append(t1)
    travelers.append(t2)

    # booking
    booking1 = BookingSystem()
    print(booking1.booking(trip1, contact, travelers))