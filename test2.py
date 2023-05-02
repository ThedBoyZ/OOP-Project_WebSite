import asyncio
import motor.motor_asyncio

async def insert_document():
    # Connect to the MongoDB database
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
    db = client["mydatabase"]

    # Access a collection
    users = db.users

    # Insert a document into the collection
    user = {"name": "John", "age": 30}
    result = await users.insert_one(user)
    print("Inserted document with ID:", result.inserted_id)

# Run the insert_document function asynchronously
asyncio.run(insert_document())