from system import System

class TestPayment:
    def __init__(self):
        self.price = 1200
    
    def make_payment(self, email, amount):
        if amount == self.price:
            System.write_purchased(email, amount)
        else:
            print("payment incomplete")

TestPayment().make_payment("pinguuux@", 1200)