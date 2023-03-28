from Payment import Payment
from Payment import PaymentCollection

class Booking:
    def __init__(self, status, typestravel, order_code, total_price, transaction_id):
        self.__status = status
        self.__typetravel = typestravel
        self.__order_code = order_code
        self.__total_price = total_price
        self.__transaction_id = transaction_id
    
    def check_booking_status():
        pass

class BookingCollection:
    def __init__(self, booking):
        self.__booking_list = []
        for attr in booking:
            if isinstance(attr, Booking):
                self.__booking_list.append(attr)

    def get_status(self, index):
        return self.__booking_list[index]._Booking__status
    
    def get_typetravel(self, index):
        return self.__booking_list[index]._Booking__typetravel
    
    def get_order_code(self, index):
        return self.__booking_list[index]._Booking__order_code
      
    def get_total_price(self, index):
        return self.__booking_list[index]._Booking__total_price
    
    def get_transaction_id(self, index):
        return self.__booking_list[index]._Booking__transaction_id
    
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
            
# Create 3 instances from Booking
book1 = Booking('Completed', ['adult'], '5001', 1500, '3001')       
book2 = Booking('Waiting', ['adult', 'child'], '5002', 1000, '3002') 
book3 = Booking('Completed', ['adult', 'infant'], '5003', 1290, '3003')  

# Collect 3 instances from Booking in BookingCollection
booking_list = BookingCollection([book1, book2, book3])

# Create 3 instances from Payment
payment1 = Payment('InternetBanking', 'THB', 'SCB', 'Need Payment', '18:20', '3001')
payment2 = Payment('Paypal', 'THB', 'SCB', 'Payment Completed', '14:07', '3002')
payment3 = Payment('CreditCard', 'THB', 'SCB', 'Payment Completed', '02:23', '3003')

# Collect 3 instances from Payment in PaymentCollection
payment_list = PaymentCollection([payment1, payment2, payment3])

# UI --> Enter 1 or 2
choice = int(input('Check Orders by\n(1) Airpaz Code  (2) Booking Status\n'))
if choice == 1:
    order_code = input('Enter Your Airpaz Code: ')
    # Search Booking by using order code
    order_code_index = booking_list.check_order_code(order_code)
    print('-' * 50)
    if order_code_index >= 0:
        print(f'Airpaz Code: {booking_list.get_order_code(order_code_index)}')
        print(f'Booking Status: {booking_list.get_status(order_code_index)}')
        print(f'Payment Status: {payment_list.get_payment_status(order_code_index)}')
        print(f'Traveler: {booking_list.get_typetravel(order_code_index)}')
        print(f'Total Price: {booking_list.get_total_price(order_code_index)}')
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
            print(f'Booking Status: {booking_list.get_status(index)}')
            print(f'Payment Status: {payment_list.get_payment_status(index)}')
            print(f'Airpaz Code: {booking_list.get_order_code(index)}')
            print(f'Traveler: {booking_list.get_typetravel(index)}')
            print(f'Total Price: {booking_list.get_total_price(index)}')
            print('-' * 50)
    else:
        print('No Data')
        print('-' * 50)
        
# Check orders by using order code (Airpaz code)
# print(booking_list.check_order_code('1000'))

# Check orders by filtering booking status
# print(booking_list.check_booking_status('completed'))