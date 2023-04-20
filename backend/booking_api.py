from fastapi import FastAPI
from booking import *
from total_price import *
from flight import Flight, Trip
from account import Traveler, Contact


app = FastAPI()


# selected flight
flight1 = Flight("VZ100", "BKK", "CNX", "Monday", "2023-03-27 10:00", "2023-03-27 12:30", "Thai Vietjet Air")
trip1 = Trip()
trip1.add_flight(flight1)


# booking
booking_system = BookingSystem()


@app.post("/booking", tags=["booking"])
async def booking(data: dict):
    trip = trip1.get_trip_detail()
    contact = Contact(data['contact_name'], data['contact_surname'], data['contact_title'], data['contact_email'], data['contact_mobile'])
    travelers = []
    
    for i in range(data['number_of_traveler']):
        traveler_data = data['travelers'][i]
        traveler = Traveler(traveler_data['type_person'], traveler_data['title'], traveler_data['gender'], traveler_data['name'], traveler_data['surname'], traveler_data['dob'], traveler_data['nationality'])
        travelers.append(traveler)

    booking_id = booking_system.booking(trip, contact, travelers)
    return {"booking_id": booking_id}


@app.get("/booking/get_booking/{booking_id}", tags=["booking"])
async def booking(booking_id: str):
    booking = booking_system.get_booking_by_id(booking_id)
    return booking


@app.put("/booking/add_ons/{id}", tags=["booking"])
def add_ons_baggage(id: str, traveler_index: int, baggage_weight: int):
    booking = booking_system.get_booking_by_id(id)
    if booking:
        booking_system.travelers[traveler_index].baggage_weight = baggage_weight
        price_detail = PriceDetailCollection()
        for traveler in booking_system.travelers:
            price_detail.add_price_detail(traveler)
        new_price = price_detail.total_price()
        booking_system.total_price = new_price
        return {"travelers_info_update": booking_system.travelers[traveler_index].get_traveler_info()}
    else:
        return {"status": "error", "message": "Booking not found"}
    
