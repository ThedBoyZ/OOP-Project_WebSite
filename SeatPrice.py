from TravelerInfo import Traveler
from Coupon import coupon_list

class SeatPrice:
    def __init__(self, order_code, departure_airport_value, arrival_airport_value, departure_day, travelers:list):
        self.__departure_day = departure_day
        self.__order_code = order_code
        self.__distance_index = abs(departure_airport_value - arrival_airport_value)
        self.__travelers = travelers
        self.__adult = 0
        self.__child = 0
        self.__infant = 0
        self.__price_per_person = 850
        self.__total_price = 0
        for traveler in self.__travelers:
            if traveler.type_person == 'adult':
                self.__adult += 1
            elif traveler.type_person == 'child':
                self.__child += 1
            elif traveler.type_person == 'infant':
                self.__infant += 1

    def seat_price_calculator(self, promo_code = '0'):
        # Let an infant price is cheaper than an adult price around 3x
        self.__price_per_person += self.__distance_index * 50
        self.__total_price = ((self.__adult + self.__child) * self.__price_per_person) + (self.__infant * self.__price_per_person / 3)
        if self.__departure_day == 'Saturday' or self.__departure_day == 'Sunday':
            self.__total_price += (100 * (self.__adult + self.__child))
        for coupon in coupon_list._coupon_detail:
            if promo_code == coupon.code:
                self.__total_price = self.__total_price * (100 - coupon.discount) / 100
        return self.__total_price