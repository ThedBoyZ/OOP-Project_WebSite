from Payment import Payment
from Payment import PaymentCollection
from Payment import payment_list
from TravelerInfo import Traveler
from TravelerInfo import traveler1_1
from TravelerInfo import traveler2_1
from TravelerInfo import traveler2_2
from TravelerInfo import traveler3_1
from TravelerInfo import traveler3_2
from ContactInfo import ContactInfo
from ContactInfo import contact1
from ContactInfo import contact2
from ContactInfo import contact3
from Flight import Flight
from Flight import bkk_to_cnx
from Flight import cnx_to_bkk
from Flight import dmk_to_cnx
from Coupon import Coupon
from Coupon import CouponCollection
from Coupon import coupon_list
from SeatPrice import SeatPrice
from datetime import date


class Booking:
    def __init__(self, status, traveler, order_code, total_price, transaction_id, contact_info, flight):
        self.__status = status
        self.__traveler = traveler
        self.__order_code = order_code
        self.__total_price = total_price
        self.__transaction_id = transaction_id
        self.__contact_info = contact_info
        self.__flight = flight
    
class BookingCollection:
    def __init__(self):
        self.__booking_list = []
        
    def add_booking(self, booking):
        self.__booking_list.append(booking)

    def get_status(self, index):
        return self.__booking_list[index]._Booking__status
    
    def get_traveler(self, index):
        return self.__booking_list[index]._Booking__traveler
    
    def get_order_code(self, index):
        return self.__booking_list[index]._Booking__order_code
      
    def get_total_price(self, index):
        return self.__booking_list[index]._Booking__total_price
    
    def get_transaction_id(self, index):
        return self.__booking_list[index]._Booking__transaction_id
    
    def get_contact_info(self, index):
        return self.__booking_list[index]._Booking__contact_info
    
    def get_flight(self, index):
        return self.__booking_list[index]._Booking__flight
    
    # Search Booking by using order_code (Airpaz code)
    def check_order_code(self, order_code):
        for index in range(0, 3):
            if order_code == self.__booking_list[index]._Booking__order_code:
                return index
            # In case: User enter an invalid order code
            elif index == 2:
                return -1

    # Search Booking by filtering booking status
    def check_booking_status(self, status):
        index_list = []
        for index in range(0, 3):
            if status == self.__booking_list[index]._Booking__status:
                index_list.append(index)
        return index_list

seat_price1 = SeatPrice('5001', 1, 4, bkk_to_cnx.departure_day, [traveler1_1])
seat_price2 = SeatPrice('5002', 4, 1, cnx_to_bkk.departure_day, [traveler2_1, traveler2_2])
seat_price3 = SeatPrice('5003', 1, 4, dmk_to_cnx.departure_day, [traveler3_1, traveler3_2])

# Collect 3 instances from Booking in BookingCollection
booking_list = BookingCollection()

# Create 3 instances from Booking
booking_list.add_booking(Booking('Completed', [traveler1_1], '5001', seat_price1.seat_price_calculator('dc20'), '3001', contact1, [bkk_to_cnx]))
booking_list.add_booking(Booking('Waiting', [traveler2_1, traveler2_2], '5002', seat_price2.seat_price_calculator(), '3002', contact2, [cnx_to_bkk]))
booking_list.add_booking(Booking('Completed', [traveler3_1, traveler3_2], '5003', seat_price3.seat_price_calculator(), '3003', contact3, [dmk_to_cnx]))

# UI --> Enter 1 or 2
if __name__ == '__main__':
    choice = int(input('Check Orders by\n(1) Airpaz Code  (2) Booking Status\n'))
    if choice == 1:
        order_code = input('Enter Your Airpaz Code: ')
        # Search Booking by using order code
        order_code_index = booking_list.check_order_code(order_code)
        print('-' * 50)
        if order_code_index >= 0:
            print(f'Airpaz Code: {booking_list.get_order_code(order_code_index)}')
            print(f'Booking Status: {booking_list.get_status(order_code_index)}')
            transaction_index = payment_list.check_payment_status(booking_list.get_transaction_id(order_code_index))
            print(f'Payment Status: {payment_list.get_payment_status(transaction_index)}')
            for traveler in booking_list.get_traveler(order_code_index):
                print(f'Traveler: {traveler.title} {traveler.name} {traveler.surname}\nNationality: {traveler.nationality}  Date of Birth: {traveler.date_of_birth}')
            for flight in booking_list.get_flight(order_code_index):
                print(f'Departure: {flight.departure_airport} {flight.departure_day} {flight.departure_time}\nArrival: {flight.arrival_airport} {flight.arrival_day} {flight.arrival_time}')
            print(f'Total Price: {booking_list.get_total_price(order_code_index):.2f}')
        else:
            print('No Data')
        print('-' * 50)
    elif choice == 2:
        status = input('Select Booking Status\n(1) Confirmed  (2) Completed  (3) Waiting  (4) Cancelled\n')
        # Status Dictionary
        if status == '1':
            status = 'Confirmed'
        elif status == '2':
            status = 'Completed'
        elif status == '3':
            status = 'Waiting'
        elif status == '4':
            status = 'Cancelled'
        status_index = booking_list.check_booking_status(status)
        print('-' * 50)
        if status_index != []:
            for index in status_index:
                print(f'Airpaz Code: {booking_list.get_order_code(index)}')
                print(f'Booking Status: {booking_list.get_status(index)}')
                transaction_index = payment_list.check_payment_status(booking_list.get_transaction_id(index))
                print(f'Payment Status: {payment_list.get_payment_status(transaction_index)}')
                for traveler in booking_list.get_traveler(index):
                    print(f'Traveler: {traveler.title} {traveler.name} {traveler.surname}\nNationality: {traveler.nationality}  Date of Birth: {traveler.date_of_birth}')
                for flight in booking_list.get_flight(index):
                    print(f'Departure: {flight.departure_airport} {flight.departure_day} {flight.departure_time}\nArrival: {flight.arrival_airport} {flight.arrival_day} {flight.arrival_time}')
                print(f'Total Price: {booking_list.get_total_price(index):.2f}')
                print('-' * 50)
        else:
            print('No Data')
            print('-' * 50)