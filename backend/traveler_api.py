from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from account import Traveler

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

@app.post("/add_traveler", tags=["traveler"])
async def add_traveler(data: dict):
    traveler = Traveler(data['type_person'], data['title'], data['gender'], data['name'], data['surname'], data['dob'], data['nationality'], data['baggage_weight'])
    return {"details": traveler.get_traveler_info()}