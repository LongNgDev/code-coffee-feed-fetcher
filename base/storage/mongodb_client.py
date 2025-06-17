from abc import ABC
from pymongo import MongoClient
from datetime import datetime, timezone

from base.storage.db_interface import DatabaseInterface


class MongoDBClient(DatabaseInterface, ABC):
    def __init__(self, collection_name:str, uri: str = "mongodb://127.0.0.1:27017/", db_name: str = "code_and_coffee_db"):
        self.uri = uri
        self.db_name = db_name
        self.db_collection_name = collection_name
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        print(f"✅ Connected to MongoDB database: {self.db_name}")

    def connect(self):
        """Reconnect to the MongoDB database if disconnected."""
        if not self.client:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"✅ Reconnected to MongoDB database: {self.db_name}")

    def disconnect(self):
        """Disconnect from the MongoDB database."""
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print(f"🛑 Disconnected from MongoDB database: {self.db_name}")

    def save(self, data: dict):
        """Save data to the database with duplicate check."""
        if not data:
            print("⚠️ No data to save.")
            return
        
        collection = self.get_collection()

        # Check for duplicates before saving
        if self.is_duplicate(data):
            print(f"⚠️ Duplicate not saved: {data.get('title', 'Untitled')}")
            return
        
        # Add timestamp if not present
        if "saved_at" not in data:
            data["saved_at"] = datetime.now(timezone.utc)

        collection.insert_one(data)
        print(f"✅ Saved item to {self.db_collection_name}: {data.get('title', 'Untitled')}")

    def fetch(self, query: dict):
        """Fetch data from the database."""
        collection = self.get_collection()
        return list(collection.find(query))

    def delete(self, query: dict):
        """Delete data from the database."""
        collection = self.get_collection()
        result = collection.delete_many(query)
        print(f"🗑️ Deleted {result.deleted_count} documents from {self.db_collection_name}")

    def update(self, query: dict, update_data: dict):
        """Update data in the database."""
        collection = self.get_collection()
        result = collection.update_one(query, {"$set": update_data})
        print(f"🔄 Updated {result.modified_count} documents in {self.db_collection_name}")

    def update_many(self, query: dict, update_data: dict):  
        """Update data in the database."""
        collection = self.get_collection()
        result = collection.update_many(query, {"$set": update_data})
        print(f"🔄 Updated {result.modified_count} documents in {self.db_collection_name}")

    """ def update_many """

    def clear(self):
        """Clear the specified collection."""
        collection = self.get_collection()
        collection.delete_many({})
        print(f"🗑️ Cleared the collection: {self.db_collection_name}")

    def get_collection(self):
        """Get a specific collection from the database."""
        return self.db[self.db_collection_name]
    
    def get_all_collections(self):
        """Get all collections in the database."""
        return self.db.list_collection_names()

    def is_duplicate(self, data: dict) -> bool:
        """Check if data already exists by unique keys like guid or link."""
        collection = self.get_collection()
        query = {"$or": []}

        # Check for unique fields like "guid" or "link"
        if "guid" in data and data["guid"]:
            query["$or"].append({"guid": data["guid"]})
        if "link" in data and data["link"]:
            query["$or"].append({"link": data["link"]})

        # If no unique fields provided, return False (not a duplicate)
        if not query["$or"]:
            return False

        # Check for existing document
        existing_document = collection.find_one(query)
        return existing_document is not None

