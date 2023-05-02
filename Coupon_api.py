from typing import Union
from fastapi import FastAPI
from Coupon import Coupon
from Coupon import CouponCollection
from Coupon import coupon_list

app = FastAPI()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Hello": "World"}

@app.get("/coupon_home", tags=['Coupon'])
async def get_coupon() -> object:
    return {"Data": coupon_list}

@app.post("/add_coupon", tags=['Coupon'])
async def new_coupon(code: str, discount: int, description: str, promo_period: str, travel_period: list):
    for attr in coupon_list._coupon_detail:
        if code == attr.code:
            return "This code has already existed in a system"
        else:
            pass
    coupon_object = Coupon(code, discount, description, promo_period, travel_period)
    coupon_list.add_coupon(coupon_object)
    return {
        "data": "New coupon is added"
    }

@app.delete("/delete_coupon", tags=['Coupon'])
async def delete_coupon(code: str):
    index = 0
    for attr in coupon_list._coupon_detail:
        if code != attr.code:
            index += 1
        else:
            break
    deleted_coupon = coupon_list.delete_coupon(index)
    return {
        'data' : f'Coupon code: {deleted_coupon.code} has been deleted'
    }
    