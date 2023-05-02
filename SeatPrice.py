from TravelerInfo import traveler1_1
from TravelerInfo import traveler2_1
from TravelerInfo import traveler2_2
from TravelerInfo import traveler3_1
from TravelerInfo import traveler3_2
from Flight import bkk_to_cnx
from Flight import cnx_to_bkk
from Flight import dmk_to_cnx
from Coupon import coupon_list

class SeatPrice:
    def __init__(self, order_code, departure_airport_value, arrival_airport_value, departure_day, travelers:list, add_on_baggage = [], promo_code = '0'):
        add_on_baggage_dict = {0 : 0, 15 : 400, 20 : 450, 25 : 600, 30 : 900, 35 : 1100, 40 : 1400}
        self.__departure_day = departure_day
        self.__order_code = order_code
        self.__distance_index = abs(departure_airport_value - arrival_airport_value)
        self.__travelers = travelers
        self.__adult = 0
        self.__child = 0
        self.__infant = 0
        self.__price_per_person = 850
        self.__promo_code = promo_code
        self.__add_on_baggage = add_on_baggage
        self.__add_on_price = 0
        self._total_price = 0
        self._total_discount = 0
        for traveler in self.__travelers:
            if traveler.type_person == 'adult':
                self.__adult += 1
            elif traveler.type_person == 'child':
                self.__child += 1
            elif traveler.type_person == 'infant':
                self.__infant += 1
        for baggage in self.__add_on_baggage:
            self.__add_on_price += add_on_baggage_dict[baggage]

        # Let an infant price is cheaper than an adult price around 3x
        self.__price_per_person += self.__distance_index * 50
        self._total_price = ((self.__adult + self.__child) * self.__price_per_person) + (self.__infant * 300) + self.__add_on_price
        if self.__departure_day == 'Saturday' or self.__departure_day == 'Sunday':
            self._total_price += (100 * (self.__adult + self.__child))
        for coupon in coupon_list._coupon_detail:
            if self.__promo_code == coupon['code']:
                self._total_discount = self._total_price * coupon['discount'] / 100
                self._total_price -= self._total_discount             

    def apply_new_coupon(self, new_coupon):
        for coupon in coupon_list._coupon_detail:
            if new_coupon == coupon.code:
                self._total_price += self._total_discount
                self._total_discount = self._total_price * coupon.discount / 100
                self._total_price -= self._total_discount
        return self._total_price      

    def get_order_code(self):
        return self.__order_code
    
    def get_total_price(self):
        return self._total_price

class SeatPriceCollection: 
    def __init__(self):
        self.__seat_price_list = []

    def add_seat_price(self, seat_price):
        self.__seat_price_list.append(seat_price)

    def get_seat_price_list(self, index):
        return self.__seat_price_list[index]
    
    @property
    def seat_price_list(self):
        return self.__seat_price_list

seat_price_list = SeatPriceCollection()  

seat_price_list.add_seat_price(SeatPrice('5001', 1, 4, bkk_to_cnx.departure_day, [traveler1_1], [traveler1_1.add_on_baggage_weight], 'dc20', ))
seat_price_list.add_seat_price(SeatPrice('5002', 4, 1, cnx_to_bkk.departure_day, [traveler2_1, traveler2_2], [traveler2_1.add_on_baggage_weight, traveler2_2.add_on_baggage_weight] ))
seat_price_list.add_seat_price(SeatPrice('5003', 1, 4, dmk_to_cnx.departure_day, [traveler3_1, traveler3_2], [traveler3_1.add_on_baggage_weight, traveler3_2.add_on_baggage_weight]))