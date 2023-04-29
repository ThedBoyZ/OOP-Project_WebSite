from fastapi import FastAPI
from flight import Trip
 
app = FastAPI()
my_trip = Trip()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Air": "Paz"}

@app.post("/search_flight", tags=["search flight api"])
async def search_flight(depart, arrival, travelday):
    search_flight = my_trip.search_flight(depart, arrival, travelday)
    return {"matching_flights": search_flight}