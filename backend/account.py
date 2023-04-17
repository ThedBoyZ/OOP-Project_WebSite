from datetime import date


class Account:
    def __init__(self, name, surname, email, password, status):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__status = status      # online, offline

    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    @property
    def status(self):
        return self.__status


class Admin(Account):
    def __init__(self, name, surname, email, password, status, permission):
        Account.__init__(self, name, surname, email, password, status)
        self.__permission = permission

    @property
    def permission(self):
        return self.__permission


class User(Account):
    def __init__(self, user_id, name, surname, email, password, mobile, country, status="Offline"):
        Account.__init__(self, name, surname, email, password, status)
        self.__user_id = user_id
        self.__mobile = mobile
        self.__country = country

    def get_user_detail(self):
        return {
            "user_id": self.__user_id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password": self.password,
            "country": self.__country,
            "mobile": self.__mobile,
            "status": self.status,
        }
    

class Contact:
    def __init__(self, name, surname, title, email, mobile):
        self.__name = name
        self.__surname = surname
        self.__title = title
        self.__email = email
        self.__mobile = mobile

    def get_contact_info(self):
        return {
            "name": self.__name,
            "surname": self.__surname,
            "title": self.__title,
            "email": self.__email,
            "mobile": self.__mobile
        }


class Traveler:
    def __init__(self, type_person, title, gender, name, surname, dob, nationality):
        self.__type_person = type_person
        self.__title = title
        self.__gender = gender
        self.__name = name
        self.__surname = surname
        self.__dob = dob
        self.__nationality = nationality
        self.__baggage_weight = 0
    
    @property
    def type_person(self):
        return self.__type_person
    
    @property
    def baggage_weight(self):
        return self.__baggage_weight
    
    @baggage_weight.setter
    def baggage_weight(self, baggage_weight):
        self.__baggage_weight = baggage_weight

    def get_traveler_info(self):
        return {
            'type_person': self.type_person,
            'name': self.__name,
            'surname': self.__surname,
            'gender': self.__gender,
            'title': self.__title,
            'dob': self.__dob,
            'nationality': self.__nationality,
            'baggage_weight': self.baggage_weight
        }