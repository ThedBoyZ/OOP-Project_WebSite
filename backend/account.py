from system import System


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
            if self.__email in str(list(System.read_data().keys())) and self.__password == str(System.read_data()[f'{self.__email}']['password']):
                print("login complete")
                #User.set_user_detail(self.__email, self.__name, "Customer")
                self._email = self.__email
                if self.__email == "admin@":
                    self._status = "admin"
                else:
                    self._status = "customer"
                return self._status
            else:
                print("wrong username or password")
                self._status = "guest"
                return self._status
        except KeyError or str(System.read_data()[f"{self.__email}"]) != self.__password:
            print("wrong username or password")
            self._status = "guest"
            return self._status        


    def register(self,name , surname, email, password, confirm_password, country):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.__country = country

        self.__customer_detail = []

        self.__customer_detail.extend([self.__name, self.__surname, self.__email, self.__password, self.__country])

        if self.__email == 'root@' or self.__email == 'admin@':
            return "Invalid"
        elif self.__email not in str(list(System.read_data().keys())) and self.__password == self.__confirm_password:
            System.write_data(self.__customer_detail)
            print(self.__customer_detail)
            
            return "Register complete"
        elif self.__email in str(list(System.read_data().keys())) and self.__password == self.__confirm_password:
            return "Already registered"
        elif self.__password != self.__confirm_password:
            return "Password Not Match"
        

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

    def see_data(self, email):
        return System.search_data_by_email(email)
    

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
    def __init__(self, type_person, title, gender, name, surname, dob, nationality, baggage_weight="0"):
        self.__type_person = type_person
        self.__title = title
        self.__gender = gender
        self.__name = name
        self.__surname = surname
        self.__dob = dob
        self.__nationality = nationality
        self.__baggage_weight = baggage_weight
    
    @property
    def type_person(self):
        return self.__type_person
    
    @property
    def baggage_weight(self):
        return self.__baggage_weight

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