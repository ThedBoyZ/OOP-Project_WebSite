class InternetBanking:
    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number
    
    def make_payment(self, amount):
        print(f"Making payment of {amount} via {self.bank_name} internet banking, account number: {self.account_number}")

class CreditCard:
    def __init__(self, card_number, card_holder_name, expiry_date, cvv):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv
    
    def make_payment(self, amount):
        print(f"Making payment of {amount} using credit card {self.card_number} belonging to {self.card_holder_name}, with expiry date {self.expiry_date} and CVV {self.cvv}")

class DebitCard:
    def __init__(self, card_number, card_holder_name, expiry_date, cvv, pin):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.pin = pin
    
    def make_payment(self, amount):
        print(f"Making payment of {amount} using debit card {self.card_number} belonging to {self.card_holder_name}, with expiry date {self.expiry_date}, CVV {self.cvv}, and PIN {self.pin}")

class Paypal:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def make_payment(self, amount):
        print(f"Making payment of {amount} using Paypal account {self.email}")

class EWallet:
    def __init__(self, wallet_id, pin):
        self.wallet_id = wallet_id
        self.pin = pin
    
    def make_payment(self, amount):
        print(f"Making payment of {amount} using E-Wallet {self.wallet_id}")