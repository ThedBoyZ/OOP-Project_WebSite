from datetime import datetime
from copy import deepcopy
from fastapi import FastAPI
from abc import ABC, abstractmethod
from dataclasses import dataclass
from airport_and_airline import AirlineCollection,AirportCollection
from select_flight import Trip
from select_flight import Flight
from fastapi.middleware.cors import CORSMiddleware

my_trip = Trip()
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Air": "Paz"}

# @app.post("/search_flight", tags=["search flight api"])
# async def search_airline(depart,arrival,travelday):
#     search_flight = my_trip.search_flight(depart,arrival,travelday)
#     return {"status": search_flight}

@app.post("/search_flight", tags=["search flight api"])
async def search_airline(data : dict):
    search_flight = my_trip.search_flight(data["depart"],data["arrival"],data["travelday"])
    return {"status": search_flight}

@app.post("/add_flight", tags=["add flight api"])
async def add_flight(data : dict):
    flight = Flight(
                data["airline"],
                data["day"],
                data["departure_airport"],
                data["departure_day"],
                data["departure_time"],
                data["arrival_airport"],
                data["arrival_day"],
                data["arrival_time"],
                data["baggage"],
                data["refund"],
                data["reschedule"],
                data["id"],
                data["status"]
        )
    
    return {
        "airline": flight.airline,
        "day": flight.day,
        "departure_airport": flight.departure_airport,
        "departure_day": flight.departure_day,
        "departure_time": flight.departure_time,
        "arrival_airport": flight.arrival_airport,
        "arrival_day": flight.arrival_day,
        "arrival_time": flight.arrival_time,
        "baggage": flight.baggage,
        "refund": flight.refund,
        "reschedule": flight.reschedule,
        "id": flight.id,
        "status": flight.status
    }
  
