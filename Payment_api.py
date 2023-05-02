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

@app.post("/internet_banking", tags=['Payment'])
async def new_payment(booking_id):
    transaction = InternetBanking()
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}
    
@app.post("/credit_card", tags=['Payment'])
async def new_payment(booking_id):
    transaction = CreditCard()
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}

@app.post("/paypal", tags=['Payment'])
async def new_payment(booking_id):
    transaction = Paypal()
    for seat_price in seat_price_list.seat_price_list:
        if booking_id == seat_price.get_order_code():
            transaction.make_payment(seat_price.get_total_price())
    return {"Price": transaction.get_price(), "Processing Fee": transaction.get_processing_fee(), "Total_Price": transaction.get_total_price()}
