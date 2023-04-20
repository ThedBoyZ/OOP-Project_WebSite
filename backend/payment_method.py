from booking import BookingSystem

class Payment:
    def __init__(self):
        self.__amount = 0
    
    @property
    def amount(self):
        return self.__amount
    
    def calculate_total_amount(self):
        pass
    
    def make_payment(self, price):
        pass


class InternetBanking:
    def __init__(self, bank_name, account_number):
        self.__bank_name = bank_name
        self.__account_number = account_number
        self.__procession_fee = 185

    def make_payment(self, price):
        if self.calculate_total_amount() == price:
            print(f"Making payment of {self.calculate_total_amount()} via {self.__bank_name} internet banking, account number: {self.__account_number}")
            return "Complete"
        else:
            return "Incomplete"


class CreditCard(Payment):
    def __init__(self, card_number, card_holder_name, expiry_date, cvv, amount, procession_fee):
        Payment().__init__(self, amount, procession_fee)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv

    def calculate_total_amount(self):
        return self.amount + 207
    
    def make_payment(self):
        print(f"Making payment of {self.calculate_total_amount()} using credit card {self.card_number} belonging to {self.card_holder_name}, with expiry date {self.expiry_date} and CVV {self.cvv}")

class DebitCard(Payment):
    def __init__(self, card_number, card_holder_name, expiry_date, cvv, amount, procession_fee):
        Payment().__init__(self, amount, procession_fee)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv

    def calculate_total_amount(self):
        return self.amount + 207
    
    def make_payment(self):
        print(f"Making payment of {self.calculate_total_amount()} using debit card {self.card_number} belonging to {self.card_holder_name}, with expiry date {self.expiry_date} and CVV {self.cvv}")

class Paypal(Payment):
    def __init__(self, email, password, amount):
        Payment().__init__(self, amount)
        self.email = email
        self.password = password

    def calculate_total_amount(self):
        return self.amount + 150
    
    def make_payment(self):
        print(f"Making payment of {self.amount} using Paypal account {self.email}")

class TruemoneyWallet(Payment):
    def __init__(self, phone, amount):
        Payment().__init__(self, amount)
        self.phone = phone

    def calculate_total_amount(self):
        return self.amount + 208
    
    def make_payment(self):
        print(f"Making payment of {self.amount} using E-Wallet {self.wallet_id}")


if __name__ == "__main__":
    payment = InternetBanking('SCB', '0242842276')
    print(payment.make_payment(1200))