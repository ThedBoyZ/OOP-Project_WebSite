from typing import Union
from fastapi import FastAPI
from Payment_page import Payment
from Payment_page import InternetBanking
from Payment_page import CreditCard
from Payment_page import Paypal
from Check_orders_for_customer import booking_list
from SeatPrice import seat_price_list

app = FastAPI()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Hello": "World"}

@app.get("/payment", tags=['Payment'])
async def get_total_price(booking_id: str):
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            return {"Price": seat_price.get_total_price()}
    return 'No Data'

@app.post("/payment_method", tags=['Payment'])
async def new_payment(payment_method: str):
    return payment_method # Want to change path to each of payment method

@app.post("/payment_method/InternetBanking", tags=['Payment'])
async def new_payment(booking_id, bank_name, account_number):
    transaction = InternetBanking(bank_name, account_number)
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}
    
@app.post("/payment_method/CreditCard", tags=['Payment'])
async def new_payment(booking_id, card_number, card_holder_name, expiry_date, cvv):
    transaction = CreditCard(card_number, card_holder_name, expiry_date, cvv)
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}

@app.post("/payment_method/Paypal", tags=['Payment'])
async def new_payment(booking_id, email, password):
    transaction = Paypal(email, password)
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}

