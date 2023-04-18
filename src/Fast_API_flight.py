from datetime import datetime
from copy import deepcopy
from fastapi import FastAPI
from abc import ABC, abstractmethod
from dataclasses import dataclass
from airport_and_airline import AirlineCollection,AirportCollection
from select_flight import Trip
 
my_trip = Trip()
app = FastAPI()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Air": "Paz"}

@app.post("/search_flight", tags=["search flight api"])
async def search_airline(depart,arrival,travelday):
    search_flight = my_trip.search_flight(depart,arrival,travelday)
    return {"status": search_flight}
