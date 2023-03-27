import hashlib
from system import System

#Actor = User

class Account:
    def __init__(self, name, surname, email, password, status):
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password
        self._status = status


    def login(self, email, password):
        self._email = email
        self._encoded_password = password.encode()

        #self.__hashed_password = hashlib.sha256(self._encoded_password).hexdigest()
        
        try:
            if self._email in str(list(System.read_data().keys())) and self._password == str(System.read_data()[f'{self._email}']):
                print("complete")
               
        except KeyError:
            print("wrong")

p1 = Account("ping", "pong", "gmail", "1234", "1")

p1.login("Admin", "1234")
