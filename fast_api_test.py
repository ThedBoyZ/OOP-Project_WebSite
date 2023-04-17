from typing import Optional,Dict
from fastapi import FastAPI,HTTPException

from system import System
from test import User
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

# @app.post("/login", tags=["Login"])
# async def login(email:dict, password:dict):
#     login_status = p1.login(email, password)

#     if(login_status=="guest"):
#         return {"login_status":"incomplete"}
#     elif(login_status == "customer"):
#         return {"login_status":"complete","login_as":f"{email}"}

@app.post("/login", tags=["Login"])
async def login(body : dict) -> dict:
    email = body.get("email")
    password = body.get("password")
    login_status = p1.login(email, password)

    if login_status == "guest":
        return {"login_status": "incomplete"}
    elif login_status == "customer":
        return {"login_status": "complete", "login_as": email}
    
    

@app.post("/register", tags=["Register"])
async def register(data : dict) -> dict:
    __name = data["name"]
    __surname = data["surname"]
    __email = data["email"]
    __password = data["password"]
    __confirm_password = data["confirm_password"]
    __country = data["country"]
    return {
            "register_status":p1.register(__name, __surname, __email, __password, __confirm_password, __country),
            "registered_data":p1.see_data(__email)
            # "register_status": p1.register(data["name"],data["surname"],data["email"],data["password"],data["confirm_password"],data["country"]),
            # "registered_data": {p1.see_data(data["email"])}
            }

@app.post("/user_data", tags=["UserData"])
async def user_data(data : dict) -> dict:
    return {"user_data":p1.see_data(data["data"])}
    #print(data["data"])


@app.get("/user/{id}")
async def put_id(id):
    return f"Hello {id}"

# @app.post("/refund", tags=["Refund"])
# async def refund():

