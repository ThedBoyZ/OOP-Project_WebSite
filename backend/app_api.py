from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from booking import *
from total_price import *
from flight import Trip
from account import Traveler, Contact


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# search flights
trip1 = Trip()
my_trip = trip1.search_flight('BKK', 'CNX', 'Friday')

# booking
booking_system = BookingSystem()


@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Air": "Paz"}

# --------------------------------- Search Flight -------------------------------------

@app.post("/search_flight", tags=["search flight"])
async def search_flight(depart, arrival, travelday):
    search_flight = trip1.search_flight(depart, arrival, travelday)
    return {"matching_flights": search_flight}

# ---------------------------------- Booking ------------------------------------------

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
    booking_details = booking_system.get_booking_by_id(airpaz_code)
    return {"booking_details": booking_details}

@app.get("/booking/{airpaz_code}", tags=["booking"])
async def get_booking(airpaz_code: str):
    booking_details = booking_system.get_booking_by_id(airpaz_code)
    return {"booking_details": booking_details}

# ---------------------------------- Total price ----------------------------------------

@app.post("/discount", tags=["discount"])
async def discount(data: dict):
    travelers = []
    for i in range(int(data['number_of_traveler'])):
        traveler_data = data['travelers'][i]
        traveler = Traveler(traveler_data['type_person'], traveler_data['title'], traveler_data['gender'], traveler_data['name'], traveler_data['surname'], traveler_data['dob'], traveler_data['nationality'], traveler_data['baggage_weight'])
        travelers.append(traveler)

    details = PriceDetailCollection(my_trip[2], travelers)
    details.discount(data['promo_code'])
    return {"Update_price_details": details.get_price_details()}