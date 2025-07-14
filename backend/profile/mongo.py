from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
COMPASS_DB_NAME = os.getenv("COMPASS_DB_NAME", "Smart_resume")
COMPASS_COLLECTION_NAME =  os.getenv("COMPASS_COLLECTION_NAME", "users")
client = AsyncIOMotorClient(MONGO_URI)

db = client[COMPASS_DB_NAME]  # Matches your Compass DB name
student_collection = db[COMPASS_COLLECTION_NAME]  # Matches your Compass Collection name