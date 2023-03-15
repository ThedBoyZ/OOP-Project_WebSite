class TravelerInfo:
    def __init__(self, type_person, user_id, title, name, surname, birth, nationality):
        self._type_person = type_person
        self.__user_id = user_id
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__birth = birth
        self.__nationality = nationality

class ContactInfo:
    def __init__(self, select_contact, title, name, surname, country, mobile, email):
        self.__select_contact = select_contact
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__country = country
        self.__mobile = mobile
        self.__email = email

class SeatPrice:
    def __init__(self, price):
        self.price = price

class AddOn:
    def __init__(self, type_person, add_on_baggage):
        self.type_person = type_person
        self.add_on_baggage = add_on_baggage