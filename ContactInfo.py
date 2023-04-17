class ContactInfo:
    def __init__(self, title, name, surname, country, mobile, email, select_contact = 'adult'):
        self.__select_contact = select_contact
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__country = country
        self.__mobile = mobile
        self.__email = email

    @property
    def select_contact(self):
        return self.__select_contact
    
    @property
    def title(self):
        return self.__title 
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def country(self):
        return self.__country
    
    @property
    def mobile(self):
        return self.__mobile
    
    @property
    def email(self):
        return self.__email

contact1 = ContactInfo('Mr.', 'Pita', 'Pati', 'Thailand', '0123456789', 'pita@gmail.com', None)
contact2 = ContactInfo('Mr.', 'Prayad', 'Monday', 'Congo', '0112223333', 'prayad@gmail.com', None)
contact3 = ContactInfo('Mrs.', 'Jinny', 'Jay', 'USA', '0555555555', 'jinjin@gmail.com', None)