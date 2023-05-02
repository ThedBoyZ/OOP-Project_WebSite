from datetime import date

class Traveler:
    def __init__(self, type_person, title, gender, name, surname, date_of_birth, nationality, add_on_bagagge_weight = 0):
        self.__type_person = type_person
        self.__title = title
        self.__gender = gender
        self.__name = name
        self.__surname = surname
        self.__date_of_birth = date_of_birth
        self.__nationality = nationality
        self.__add_on_baggage_weight = add_on_bagagge_weight

    @property
    def type_person(self):
        return self.__type_person
    
    @property
    def title(self):
        return self.__title 
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def date_of_birth(self):
        return self.__date_of_birth
    
    @property
    def nationality(self):
        return self.__nationality
    
    @property
    def add_on_baggage_weight(self):
        return self.__add_on_baggage_weight
    
    @property
    def traveler_dict(self):
        return vars(self)

traveler1_1 = Traveler('adult', 'Mr.', 'male', 'Pita', 'Pati', date(1990, 10, 20), 'Thai', 20)
traveler2_1 = Traveler('adult', 'Mr.', 'male', 'Prayad', 'Monday', date(1977, 1, 21), 'Congo', 20)
traveler2_2 = Traveler('child', None, 'male', 'Pranom', 'Friday', date(2007, 3, 4), 'India', 15)
traveler3_1 = Traveler('adult', 'Mrs.', 'female', 'Jinny', 'Jay', date(1999, 7, 12), 'USA', 30)
traveler3_2 = Traveler('infant', None, 'male', 'Jude', 'Bellingham', date(2023, 2, 3), 'England', 0)