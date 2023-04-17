import requests
from datetime import datetime


class PromoCode:
    def __init__(self):
        self.__promo_code_list = []
    
    def add_promo_code(self, code):
        if code in self.__promo_code_list:
            raise ValueError("Code already exists")
        else:
            self.__promo_code_list.append(code)
    
    def remove_promo_code(self, code):
        if code in self.__promo_code_list:
            self.__promo_code_list.remove(code)
        else:
            raise ValueError("Code does not exist")
    
    def verify_code(self, code):
        if code in self.__promo_code_list:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__promo_code_list}"
    
class Payment:

    currency_dict = {
        "THB - Thai Bath" : ["Internet Banking", "Credit Card", "Debit Card", "Over The Counter", "E-Wallet", "Paypal"],
        "USD - United States Dollar" : ["Union Pay", "Credit Card", "Debit Card", "Paypal"],
    }

    def __init__(self, airpaz_code, booking_status, payment_currency, trip, traveler_details, price_details):
        self.__airpaz_code = airpaz_code
        self.__booking_status = booking_status
        self.__payment_currency = payment_currency
        self.__payment_method = self.available_payment_method(self.payment_currency)
        self.__trip = trip
        self.__traveler_details = traveler_details
        self.__price_details = price_details
    
    @staticmethod
    def available_payment_method(currency):
        return Payment.currency_dict.get(currency, [])

    @property
    def airpaz_code(self):
        return self.__airpaz_code
    
    @property
    def booking_status(self):
        return self.__booking_status

    @booking_status.setter
    def booking_status(self, status):
        self.__booking_status = status

    @property
    def payment_currency(self):
        return self.__payment_currency

    @payment_currency.setter
    def payment_currency(self, currency):
        self.__payment_currency = currency
        self.__payment_method = self.available_payment_method(currency)

    @property
    def payment_method(self):
        return self.__payment_method

    @property
    def trip(self):
        return self.__trip

    @property
    def traveler_details(self):
        return self.__traveler_details

    @property
    def price_details(self):
        return self.__price_details

    def __str__(self):
        summary = "Payment Summary:\n"
        summary += f"Airpaz Code: {self.airpaz_code}\n"
        summary += f"Booking Status: {self.booking_status}\n"
        summary += f"Payment Currency: {self.payment_currency}\n"
        summary += f"Payment Method: {', '.join(self.payment_method)}\n"
        summary += "Trip Details:\n"
        summary += f"  Departure: {self.trip['departure']}\n"
        summary += f"  Destination: {self.trip['destination']}\n"
        summary += f"  Departure Date: {self.trip['departure_date']}\n"
        summary += f"  Return Date: {self.trip['return_date']}\n"
        summary += "Traveler Details:\n"
        for traveler in self.traveler_details:
            summary += f"  Name: {traveler['name']}\n"
            summary += f"  Age: {traveler['age']}\n"
            summary += f"  Passport Number: {traveler['passport_number']}\n"
            summary += "-"*40 + "\n"
        summary += f"Total Price: {self.calculate_total_price()}\n"
        return summary


class BankAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
    
    def authenticate(self):
        url = f"{self.base_url}/auth"
        response = self.session.post(url, json={"username": self.username, "password": self.password})
        response.raise_for_status()
        return response.json()["access_token"]
    
    def initiate_payment(self, recipient, amount, access_token):
        url = f"{self.base_url}/payments"
        headers = {"Authorization": f"Bearer {access_token}"}
        data = {"recipient": recipient, "amount": amount}
        response = self.session.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["payment_id"]
    
    def authorize_payment(self, payment_id, authorization_code, access_token):
        url = f"{self.base_url}/payments/{payment_id}/authorize"
        headers = {"Authorization": f"Bearer {access_token}"}
        data = {"authorization_code": authorization_code}
        response = self.session.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["status"]
    
class InternetBanking:
    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number
    
    def make_payment(self, amount):
        print(f"Initiating payment of {amount} via {self.bank_name} internet banking, account number: {self.account_number}")
        
        # Connect to the bank's system and authenticate the user
        bank_api = BankAPI(self.account_number)
        bank_api.authenticate()
        
        # Initiate the payment with the bank's system
        recipient = input("Enter recipient name: ")
        bank_api.initiate_payment(recipient, amount)
        
        # Authorize the payment with the bank's system
        authorization_code = input("Enter authorization code: ")
        bank_api.authorize_payment(authorization_code)
        
        print(f"Payment of {amount} has been successfully made via {self.bank_name} internet banking, account number: {self.account_number}")
        

if __name__ == "__main__":
    # payment2 = Payment("AP5678", "Pending", "USD - United States Dollar", 
    #                    {"departure": "New York", "destination": "Los Angeles", "departure_date": "2023-07-01", "return_date": "2023-07-07"}, 
    #                    [{"name": "Bob Smith", "age": 40, "passport_number": "ABC123456"}, {"name": "Alice Smith", "age": 35, "passport_number": "DEF654321"}], 
    #                    {"adult": 800, "adult": 800, "infant": 300})

    # print(payment2)

    # payment2.booking_status = "Confirmed"
    # payment2.payment_currency = "THB - Thai Bath"
    # print(payment2)

    # promo_code = PromoCode()
    # promo_code.add_promo_code("ADRW14")
    # print(promo_code.verify_code("ADRW14"))

    user1_scb = InternetBanking("Siam Commercial Bank", "24781972")
    user1_scb.make_payment(100)