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
        self.__email = email
        self.__password = password
        #self.__encoded_password = password.encode()
        #self.__hashed_password = hashlib.sha256(self._encoded_password).hexdigest()
        try:
            
            if self.__email in str(list(System.read_data().keys())) and self.__password == str(System.read_data()[f'{self.__email}']):
                print("login complete")
                if(self.__email=='root@'):
                    return 'root'
                else:
                    return "customer"
                
            else:
                print("wrong username or password")
                return "guest"
        except KeyError or str(System.read_data()[f"{self.__email}"]) != self.__password:
            print("wrong")
            return "guest"

    def register(self, email, password, confirm_password):
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password

        if self.__email!=str(list(System.read_data().keys())):
            pass
        else:
            print("Already registered")

class User(Account):
    def __init__(self, name, surname, email, password, status, country, mobile, user_id, user_data_list):
        Account.__init__(self, name="Guest", surname="None", email="None", password="None", status="guest")
        self.__country = country
        self.__mobile = mobile
        self.__user_id = user_id
        self.__user_data_list = user_data_list
    
    def ValidateUser():
        pass

    def change_trip_date(self, departure_date, arrival_date):
        self.departure_date = departure_date
        self.arrival_date = arrival_date

    def set_user_status(self,status):
        self._status = status

    def __str__(self) -> str:
        return self._status

p1 = Account()
p1.register("pingping", 5678 , 5678)




