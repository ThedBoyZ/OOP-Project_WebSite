from typing import Optional,Dict
from fastapi import FastAPI,HTTPException

from system import System
# from test import User
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Coupon import Coupon
from Coupon import CouponCollection
from Coupon import coupon_list
from Payment_page import Payment, Promptpay, CreditCard, Paypal

from datetime import datetime
from copy import deepcopy
from fastapi import FastAPI
from abc import ABC, abstractmethod
from dataclasses import dataclass
from airport_and_airline import AirlineCollection,AirportCollection
from flights import Trip

from booking import *
from total_price import *

from account import User, Traveler, Contact

from database import fetch_one_todo, create, update_todo, testDB


my_trip = Trip()

app = FastAPI()

p1 = User()

booking_system = BookingSystem()

orders = Order()

origins = [
    "http://localhost:3000",
]

class loginItem(BaseModel):
    email: str
    password: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/data")
async def read_root():
    return System.read_data()

@app.post("/login", tags=["Login"])
async def login(body : dict) -> dict:
    email = body.get("email")
    password = body.get("password")
    login_status = p1.login(email, password)

    if login_status == "guest":
        return {"login_status": "incomplete"}
    elif login_status == "customer":
        return {"login_status": "complete", "login_as": email}
    elif login_status == "root":
        return {"login_status:":"root"}
    
    

@app.post("/register", tags=["Register"])
async def register(data : dict) -> dict:
    __name = data["name"]
    __surname = data["surname"]
    __email = data["email"]
    __password = data["password"]
    __confirm_password = data["confirm_password"]
    __country = data["country"]
    return {'data':p1.register(__name, __surname, __email, __password, __confirm_password, __country)}
    #return p1.register(__name, __surname, __email, __password, __confirm_password, __country)

@app.get("/see_profile", tags=['see profile'])
async def see_profile():
    return {'profile':p1.see_profile()}

@app.post("/user_data", tags=["UserData"])
async def user_data(data : dict) -> dict:
    #return {"user_data":p1.see_data(data["data"])}
    if p1.get_status() == 'admin':
        return {"user_data":p1.see_data(data["data"])}
    else:
        return {"user_data":"you dont have permission"}
    #print(data["data"])


@app.post("/search_flight", tags=["search flight api"])
async def search_airline(data : dict):
    search_flight = my_trip.search_flight(data["depart"],data["arrival"],data["travelday"])
    
    return {"respond":search_flight}

@app.get("/current_status", tags=['get current status'])
async def get_current_data():
    __status = p1.get_status()
    return {"status":__status} 



@app.get("/test")
async def test():
    search_flight = my_trip.search_flight("BKK","CNX","Thursday")
    return {"respond":search_flight}
    #return {"respond":{"data":search_flight}}
# @app.post("/refund", tags=["Refund"])
# async def refund():

@app.post("/testDB")
async def get_test(data : dict):
    
    return data["airline"]

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

@app.get("/payment_complete/{airpaz_code}", tags=['Payment'])
async def new_payment(airpaz_code: str):
    for booking in orders.booking_list:
        if airpaz_code == booking.airpaz_code:
            booking.status = "Completed"
    # return {"Status": booking.status}

@app.get("/promptpay/{airpaz_code}", tags=['Payment'])
async def new_payment(airpaz_code: str):
    transaction = Promptpay()
    for booking in orders.booking_list:
        if airpaz_code == booking.airpaz_code:
            transaction.price = int(booking.price_details["Total_price"])
            transaction.make_payment()
            # booking.status = "Completed"
    return {"Price": transaction.price, "Processing Fee": transaction.processing_fee, "Total_Price": transaction.total_price}
    
@app.get("/credit_card/{airpaz_code}", tags=['Payment'])
async def new_payment(airpaz_code: str):
    transaction = CreditCard()
    for booking in orders.booking_list:
        if airpaz_code == booking.airpaz_code:
            transaction.price = int(booking.price_details["Total_price"])
            transaction.make_payment()
            # booking.status = "Completed"
    return {"Price": transaction.price, "Processing Fee": transaction.processing_fee, "Total_Price": transaction.total_price}

@app.get("/paypal/{airpaz_code}", tags=['Payment'])
async def new_payment(airpaz_code: str):
    transaction = Paypal()
    for booking in orders.booking_list:
        if airpaz_code == booking.airpaz_code:
            transaction.price = int(booking.price_details["Total_price"])
            transaction.make_payment()
            # booking.status = "Completed"
    return {"Price": transaction.price, "Processing Fee": transaction.processing_fee, "Total_Price": transaction.total_price}

@app.post("/booking", tags=["booking"])
async def add_booking(data: dict):
    trip = data['trip_detail']
    contact = Contact(data['contact_name'], data['contact_surname'], data['contact_title'], data['contact_email'], data['contact_mobile'])
    travelers = []
    
    for i in range(int(data['number_of_traveler'])):
        traveler_data = data['travelers'][i]
        traveler = Traveler(traveler_data['type_person'], traveler_data['title'], traveler_data['gender'], traveler_data['name'], traveler_data['surname'], traveler_data['dob'], traveler_data['nationality'], traveler_data['baggage_weight'])
        travelers.append(traveler)

    airpaz_code = booking_system.booking(trip, contact, travelers)
    orders.add_booking(booking_system)
    return {"airpaz_code": airpaz_code}

@app.get("/booking/{airpaz_code}", tags=["booking"])
async def get_booking(airpaz_code: str):
    booking_details = booking_system.get_booking_by_id(airpaz_code)
    return {"booking_details": booking_details}

@app.post("/discount", tags=["discount"])
async def discount(data: dict):
    details = booking_system.get_booking_by_id(data['airpaz_code'])
    if details:  # check if booking exists
        new_price = PriceDetailCollection(details["trip_detail"], booking_system.travelers)
        res = new_price.discount(data['promo_code'])
        booking_system.price_details = new_price.get_price_details()
        return {"Status": res}
    else:
        return {"Status": "Error: Booking not found"}

@app.get("/orders/{airpaz_code}", tags=["orders"])
async def get_booking_history(airpaz_code: str):
    booking_details = orders.get_booking_by_id(airpaz_code)
    return {"booking_details": booking_details}

@app.post("/edit_account", tags=['edit account'])
async def edit_account(name, surname, country):
    return p1.edit_account(name, surname, country)