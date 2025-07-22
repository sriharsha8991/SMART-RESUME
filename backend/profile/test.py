import os
import sys
import asyncio  # Import asyncio to run async functions

# Add the backend directory to Python path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(backend_path)

# Import from profile.mongo
from mongo import *

async def main():
    # Fetch a student profile from the collection
    student = await student_collection.find_one({"email": "user@example.com"})
    
    # Test the import
    print("MongoDB connection imported successfully!")
    print(f"Database: {mongo_client.config.DB_NAME}")
    print(f"Collection: {mongo_client.config.COLLECTION_NAME}")
    collections = mongo_client.get_collection()  # This will return the collection object
    print(f"Collection object: {collections}")
    print(f"Student profile: {student}") if student else print("No student found with the given email.")

# Run the async function
asyncio.run(main())
