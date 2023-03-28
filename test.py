import hashlib
from system import System
class User:
    def __init__(self, name="guest", surname="guest", email="guest", password="guest", status="guest"):
        # self._name = name
        # self._surname = surname
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

    def register(self, email, password, confirm_password):
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password

        if self.__email not in str(list(System.read_data().keys())) and self.__password == self.__confirm_password:
            System.write_data(self.__email, self.__password)
            print("register complete")
        elif self.__password != self.__confirm_password:
            print("Password Not Match")
        else:
            print("Already registered")

    def get_user_detail(self):
        return self._status
    
    def get_user_status(self):
        return "User_status : " + self._status
    
    def set_user_detail(self, email, status):
        self.user_detail = {"email":f"{email}", "status":f"{status}"}




p1 = User()

#p1.login("ping@gmail", "1234")

# print("---Before Register---")
# print(p1.get_user_status())

# p1.login("B", "1234")

# print("---After Register---")
# p1.register("B", "1234")

# print("---Before login---")
# print(p1.get_user_status())
# print("---After login---")
# p1.login("A", "12")
# print(p1.get_user_status())

# Wrone username/password
# p1.login("c", "5678")

# p1.login("admin", "789")
# print(p1.get_user_status())

