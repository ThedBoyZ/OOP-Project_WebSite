class Account:
    def __init__(self, name, surname, email, id, password, status):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self._id = id
        self._password = password
        self._status = status

class User(Account):
    def __init__(self, country, mobile):
        Account.__init__(self, id, password, status)
        self.country = country
        self.mobile = mobile

class Admin(Account):
    def __init__(self, permission):
        Account.__init__(self, id, password, status)
        self.permission = permission

class SeatPrice:
    def __init__(self, price):
        self.price = price

class TravelerInfo:
    def __init__(self, type_person, user_id, title, name, surname, birth, nationality):
        self._type_person = type_person
        self.__user_id = user_id
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__birth = birth
        self.__nationality = nationality

class AddOn:
    def __init__(self, type_person, add_on_baggage):
        self.type_person = type_person
        self.add_on_baggage = add_on_baggage

class ContactInfo:
    def __init__(self, select_contact, title, name, surname, country, mobile, email):
        self.__select_contact = select_contact
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__country = country
        self.__mobile = mobile
        self.__email = email

class Booking:
    def __init(self, status, typestravel):
        self.__status = status
        self.__typetravel = typestravel
        
class Airport:
    def __init(self, province_name, country_name, abbreviation):
        self.__province_name = province_name
        self.__country_name = country_name
        self.__abbreviation = abbreviation

class Flight:
    def __init__(self, type_trip, id, baggage, refund, reschedule, status, \
    departure_airport, departure_date, departure_time, arrival_airport, arrival_date, arrival_time, tax):
        self.type_trip = type_trip
        self.id = id
        self.baggage = baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport = departure_airport
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_airport = arrival_airport
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.tax = tax        

class Trip:
    def __init(self, flight, count_transit):
        self._flight = flight
        self.__count_transit = count_transit

class Airline:
    def __init(self, name, logo):
        self.name = name
        self.logo = logo

class InternetBankingTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card
    
class OverTheCounterTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class EWalletTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class CreditCARDTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class DebitCardTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card


class PayPalTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class Coupon:
    def __init__(self, code, discount, description, promo_period, travel_period):
        self.code = code
        self.discount = discount
        self.description = description
        self.promo_period = promo_period
        self.travel_period = travel_period

class CouponCollection:
    def __init__(self, coupon_detail):
        self._coupon_detail = coupon_detail

