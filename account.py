import re
from datetime import date

class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

class User(Person):
    def __init__(self, name, surname, user_id, mobile_number, email, city, language, nationality, timezone):
        Person.__init__(self, name, surname)
        self.__user_id = self.remove_non_digit(user_id)
        self.__mobile_number = mobile_number
        self.__email = email
        self.__city = city
        self.__language = language
        self.__nationality = nationality
        self.__timezone = timezone

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)   # '650-1 044/3' -> '65010443'
    
class Contact(Person):
    def __init__(self, title, name, surname, country, mobile_number, email):
        Person.__init__(self, name, surname)
        self.__title = title
        self.__country = country
        self.__mobile_number = mobile_number
        self.__email = email

class Traveler(Person):
    def __init__(self, type_person, title, gender, name, surname, dob, nationality, baggage_weight):
        Person.__init__(self, name, surname)
        self.__type_person = type_person
        self.__title = title
        self.__gender = gender
        self.__dob = dob
        self.__nationality = nationality
        self.__baggage_weight = baggage_weight

        @property
        def type_person(self):
            return self.__type_person
        
        @property
        def baggage_weight(self):
            return self.__baggage_weight

class Admin(Person):
    def __init__(self, name, surname, email, permission):
        Person.__init__(self, name, surname)
        self.__email = email
        self.__permission = permission



t1 = Traveler("Adult", "Mr.", "Female", "Pim", "Niyom", date(1999, 3, 7), "Thailand", "20")
print(t1.type_person)