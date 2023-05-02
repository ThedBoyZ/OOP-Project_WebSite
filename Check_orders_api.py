from typing import Union
from fastapi import FastAPI
from Check_orders_for_customer import booking_list
from Check_orders_for_customer import seat_price_list
 

app = FastAPI()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Hello": "World"}

@app.get("/show_booking", tags=['Booking'])
async def get_booking() -> object:
    return {"Data": booking_list}

# @app.put("/apply_coupon", tags=['Coupon'])
# async def apply_coupon(order_code, coupon: str):
#     order_index = booking_list.check_order_code(order_code)
#     for seat_price in seat_price_list:
#         if order_code == seat_price.__order_code:
#             seat_price.__coupon = coupon
