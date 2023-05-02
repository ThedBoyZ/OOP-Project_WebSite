from Check_orders_for_customer import Booking
from Check_orders_for_customer import BookingCollection
from Check_orders_for_customer import booking_list
from datetime import date

class Payment:
    def __init__(self, processing_fee: int):
        self.__price = 0
        self.__total_price = 0
        self.__processing_fee = processing_fee

    def get_price(self):
        return self.__price
    
    def get_processing_fee(self):
        return self.__processing_fee
    
    def get_total_price(self):
        return self.__total_price
    
    def make_payment(self, price):
        self.__price = price
        self.__total_price = self.__price + self.__processing_fee

    def payment_completed(self, booking_id):
        booking = booking_list.get_booking_by_order_code(booking_id)
        booking.set_status('Completed')
        return booking.status()


class InternetBanking(Payment):
    def __init__(self):
        super().__init__(143)

class CreditCard(Payment):
    def __init__(self):
        super().__init__(178)

class Paypal(Payment):
    def __init__(self):
        super().__init__(166)    

if __name__ == '__name__':
    # Test InternetBanking
    # promptpay = InternetBanking('PromptPay', '490265')
    # promptpay.make_payment(1000)
    # print(f'Total Price: {promptpay.get_total_price()}')
    # print(promptpay.payment_completed('5002'))

    # Test CreditCard
    # card = CreditCard('000001', 'Kamado Tenma', date(2027, 12, 25), '213')
    # card.make_payment(1000)
    # print(f'Total Price: {card.get_total_price()}')
    # print(card.payment_completed('5001'))

    # Test Paypal
    paypal = Paypal('kadokako@gmail.com', '12345678')
    paypal.make_payment(1000)
    print(f'Total Price: {paypal.get_total_price()}')
    print(paypal.payment_completed('5001'))

    # print(f'Price: {promptpay.price()}')
    # print(f'Processing Fee: {promptpay.processing_fee()}')
    # print(f'Total Price: {promptpay.total_price()}')

