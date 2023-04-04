from datetime import date
from info import Traveler, Contact, Country
from total_price import PriceDetail, PriceDetailCollection
from flight import Flight, Trip

class Booking:
    def __init__(self, booking_id, trip, travelers, contact_info, booking_date, payment_status):
        self.booking_id = booking_id
        self.trip = trip
        self.travelers = travelers
        self.contact_info = contact_info
        self.booking_date = booking_date
        self.total_price = self.calculate_total_price(self.travelers)
        self.payment_status = payment_status

    @staticmethod
    def calculate_total_price(travelers):
        price_collection = PriceDetailCollection()
        for traveler in travelers:
            price_collection.add_price_detail(traveler)
        return price_collection.total_price()
        
    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Invalid payment amount.")

        # Check if the payment amount matches the total price
        if amount != self.total_price:
            raise ValueError("Payment amount does not match the total price.")

        # Update the payment status
        self.payment_status = "Paid"
        
    def cancel_booking(self):
        self.payment_status = "Cancelled"


class BookingCollection:
    def __init__(self):
        self._bookings = []

    def add_booking(self, booking):
        self._bookings.append(booking)

    def remove_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                self._bookings.remove(booking)
                break
            
    def check_payment_status(self):
        result = ""
        for booking in self._bookings:
            result += booking.payment_status
            result += "\n"
        return result



if __name__ == "__main__":
    # flight
    flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 18:00", "Thai Vietjet Air")
    flight2 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)

    # trip
    trip1 = Trip([flight1, flight2], count_transit=1)

    # passengers
    passenger1 = Traveler("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand", "15")
    passenger2 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand", "20")
    passenger3 = Traveler("Infant", "", "Male", "Angry", "Bird", date(2023, 3, 27), "Thailand", "0")

    # contact info
    contact1 = Contact("Mr.", "Tanathip", "Pona", "Thailand", "+66 800687960", "petch@gmail.com")

    # bookings
    booking1 = Booking("B001", trip1, [passenger1, passenger2], contact1, date.today(), "Pending")
    # print("Total price: {} bath".format(booking1.total_price))
    # print(booking1.trip)

    # booking collection
    booking_collection = BookingCollection()
    booking_collection.add_booking(booking1)

    print(booking_collection.check_payment_status())

