class Account:
    def __init__(self, name, surname, email, password, status):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__status = status

class Admin(Account):
    def __init__(self, permission):
        Account.__init__(self, name, surname, email, password, status)
        self.__permission = permission

class User(Account):
    def __init__(self, country, mobile, user_id):
        Account.__init__(self, name, surname, email, password, status)
        self.__country = country
        self.__mobile = mobile
        self.__user_id = user_id
