class Account:
    def __init__(self, name, surname, email, password, status):
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password
        self._status = status

class Admin(Account):
    def __init__(self, name, surname, email, password, status, permission):
        Account.__init__(self, name, surname, email, password, status)
        self.__permission = permission

class User(Account):
    def __init__(self, name, surname, email, password, status, country, mobile, user_id, user_data_list):
        Account.__init__(self, name, surname, email, password, status)
        self.__country = country
        self.__mobile = mobile
        self.__user_id = user_id
        self.__user_data_list = user_data_list
    
    def ValidateUser():
        pass