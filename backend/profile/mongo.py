from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

class MongoConfig:
    def __init__(self):
        load_dotenv()
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.DB_NAME = os.getenv("COMPASS_DB_NAME", "Smart_resume")
        self.COLLECTION_NAME = os.getenv("COMPASS_COLLECTION_NAME", "users")

class MongoClient:
    def __init__(self, config: MongoConfig):
        self.config = config
        self.client = AsyncIOMotorClient(config.MONGO_URI)
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
    
    def get_collection(self):
        return self.collection
    
    def get_database(self):
        return self.db

# Initialize instances
mongo_config = MongoConfig()
mongo_client = MongoClient(mongo_config)
student_collection = mongo_client.get_collection()