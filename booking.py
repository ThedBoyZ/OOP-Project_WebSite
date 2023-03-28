from datetime import date
from info import TravelerInfo, ContractInfo
from total_price import PriceDetail, PriceDetailCollection
from flight import Flight, Trip

class Booking:
    def __init__(self, booking_id, trip, passengers, contact_info, booking_date, payment_status):
        self.booking_id = booking_id
        self.trip = trip
        self.passengers = passengers
        self.contact_info = contact_info
        self.booking_date = booking_date
        self.total_price = self.calculate_total_price(self.passengers)
        self.payment_status = payment_status

    @staticmethod
    def calculate_total_price(passengers):
        price_collection = PriceDetailCollection()
        for passenger in passengers:
            price_collection.add_price_detail(passenger)
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


if __name__ == "__main__":
    # flight
    flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 18:00", "Thai Vietjet Air")
    flight2 = Flight("FD3416", "DMK", "CNX", "Tuesday", "2023-03-30 05:10", "2023-03-30 06:20", "Thai AirAsia", cabin_baggage=7, refund=False, reschedule=True)

    # trip
    trip1 = Trip([flight1, flight2], count_transit=1)

    # passengers
    passenger1 = TravelerInfo("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand", "15")
    passenger2 = TravelerInfo("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand", "20")
    passenger2 = TravelerInfo("Infant", "", "Male", "Angry", "Bird", date(2023, 3, 27), "Thailand", "0")

    # contact info
    contact_info = ContractInfo("Mr.", "Tanathip", "Pona", "Thailand", "+66 800687960", "petch@gmail.com")

    # bookings
    booking1 = Booking("B001", trip1, [passenger1, passenger2], contact_info, date.today(), "Pending")
    print(booking1.total_price)
    print(booking1.trip)