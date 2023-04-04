import hashlib
from system import System
from total_price import PriceDetailCollection
class User:
    def __init__(self, name="guest", surname="guest", email="guest", password="guest", status="guest"):
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password
        self._status = status

       # self.user_detail = {"email":f"{self._email}", "name":f"{self._name}", "status":f"{self._status}"}
    
    def ValidateUser():
        pass

    def get_status(self):
        return self._status

    def login(self, email, password):
        self.__email = email
        self.__password = password
        #self.__encoded_password = password.encode()
        #self.__hashed_password = hashlib.sha256(self._encoded_password).hexdigest()
        try:
            if self.__email in str(list(System.read_data().keys())) and self.__password == str(System.read_data()[f'{self.__email}']):
                print("login complete")
                #User.set_user_detail(self.__email, self.__name, "Customer")
                self._email = self.__email
                if self.__email == "admin":
                    self._status = "admin"
                else:
                    self._status = "customer"
            else:
                print("wrong username or password")
        except KeyError or str(System.read_data()[f"{self.__email}"]) != self.__password:
            print("wrong username or password")

    def register(self,name , surname, email, password, confirm_password, country):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.__country = country

        self.__customer_detail = []

        self.__customer_detail.extend([self.__name, self.__surname, self.__email, self.__password, self.__country])

        if self.__email not in str(list(System.read_data().keys())) and self.__password == self.__confirm_password:
            System.write_data(self.__customer_detail)
            print("register complete")
        elif self.__password != self.__confirm_password:
            print("Password Not Match")
        else:
            print("Already registered")

    def __str__(self):
        return self.__customer_detail
    
    def edit_account(self, email, name, surname, country): #return everything and save all
        exist_data = System.search_data_by_email(email)
        exist_data["name"] = name
        exist_data["surname"] = surname
        exist_data["country"] = country

        print(exist_data)

    def refund(self):
        print("refunded", System.get_purchased(self._email))
        System.reset_purchased(self._email)
        

p1 = User("Ping", "uuux", "pinguuux@", "1234", "Customer")

p1.refund()