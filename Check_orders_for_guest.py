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
from datetime import date
from Check_orders_for_customer import Booking
from Check_orders_for_customer import BookingCollection
from Check_orders_for_customer import booking_list

if __name__ == '__main__':
    # UI 
    order_code = input('Enter Your Airpaz Code: ')
    email = input('Enter Your Email: ')
    print('-' * 50)
    for index in range(0, 3):
        if order_code == booking_list.get_order_code(index) and email == booking_list.get_contact_info(index).email:
            print(f'Airpaz Code: {booking_list.get_order_code(index)}')
            print(f'Booking Status: {booking_list.get_status(index)}')
            transaction_index = payment_list.check_payment_status(booking_list.get_transaction_id(index))
            print(f'Payment Status: {payment_list.get_payment_status(transaction_index)}')
            for traveler in booking_list.get_traveler(index):
                print(f'Traveler: {traveler.title} {traveler.name} {traveler.surname}\nNationality: {traveler.nationality}  Date of Birth: {traveler.date_of_birth}')
            for flight in booking_list.get_flight(index):
                print(f'Departure: {flight.departure_airport} {flight.departure_day} {flight.departure_time}\nArrival: {flight.arrival_airport} {flight.arrival_day} {flight.arrival_time}')
            print(f'Total Price: {booking_list.get_total_price(index):.2f}')
            break
        elif index == 2:
            print('No Data')
    print('-' * 50)