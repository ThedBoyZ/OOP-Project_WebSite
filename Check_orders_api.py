from typing import Union
from fastapi import FastAPI
from Check_orders_for_customer import booking_list
from SeatPrice import seat_price_list
from SeatPrice import SeatPrice

 

app = FastAPI()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Hello": "World"}

@app.get("/show_booking", tags=['Booking'])
async def get_booking() -> object:
    return {"Data": booking_list}

@app.get("/total_price", tags=['Booking'])
async def get_total_price(order_code:str):
    for seat_price in seat_price_list.seat_price_list:
        if seat_price.order_code == order_code:
            return seat_price.total_price

@app.put("/apply_coupon", tags=['Coupon'])
async def apply_coupon(order_code: str, coupon: str):
    for seat_price in seat_price_list.seat_price_list:
        if order_code == seat_price.order_code:
            return seat_price.apply_new_coupon(coupon)
