from typing import Optional,Dict
from fastapi import FastAPI,HTTPException

from system import System
from test import User
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from datetime import datetime
from copy import deepcopy
from fastapi import FastAPI
from abc import ABC, abstractmethod
from dataclasses import dataclass
from airport_and_airline import AirlineCollection,AirportCollection
from select_flight import Trip

from database import fetch_one_todo, create, update_todo, testDB


my_trip = Trip()

app = FastAPI()

p1 = User()

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
    print(p1.register(__name, __surname, __email, __password, __confirm_password, __country))
    #return p1.register(__name, __surname, __email, __password, __confirm_password, __country)


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
