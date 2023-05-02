import motor.motor_asyncio
import asyncio
import pymongo

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

database = client["mydb"]

users = database["users"]

user = {"name":"john","age":30}
async def testDB():
    result = await users.insert_one(user)
    user_id = result.inserted_id
    print(user_id)


collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def create(todo):
    document = todo
    result = await collection.insert_one(document)
    return result

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}})
    document = await collection.find_one({"title":title})
    return document