class Account:
    def __init__(self, name, surname, email, password, status):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self._password = password
        self._status = status

class Admin(Account):
    def __init__(self, permission):
        Account.__init__(self, name, surname, email, status)
        self.permission = permission

class User(Account):
    def __init__(self, country, mobile):
        Account.__init__(self, name, surname, email, status)
        self.country = country
        self.mobile = mobile
