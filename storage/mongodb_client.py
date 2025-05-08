from pymongo import MongoClient
from datetime import datetime, timezone


class MongoDBClient:
    def __init__(self, uri: str = "mongodb://localhost:27017/", db_name: str = "code_and_coffee_db"):
        self.uri = uri
        self.db_name = db_name
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

    def save(self, data: dict, collection_name: str):
        """Save data to the database with duplicate check."""
        if not data:
            print("⚠️ No data to save.")
            return
        
        collection = self.get_collection(collection_name)

        # Check for duplicates before saving
        if self.is_duplicate(data, collection_name):
            print(f"⚠️ Duplicate not saved: {data.get('title', 'Untitled')}")
            return
        
        # Add timestamp if not present
        if "saved_at" not in data:
            data["saved_at"] = datetime.now(timezone.utc)

        collection.insert_one(data)
        print(f"✅ Saved item to {collection_name}: {data.get('title', 'Untitled')}")

    def fetch(self, query: dict, collection_name: str):
        """Fetch data from the database."""
        collection = self.get_collection(collection_name)
        return list(collection.find(query))

    def delete(self, query: dict, collection_name: str):
        """Delete data from the database."""
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query)
        print(f"🗑️ Deleted {result.deleted_count} documents from {collection_name}")

    def update(self, query: dict, update_data: dict, collection_name: str):
        """Update data in the database."""
        collection = self.get_collection(collection_name)
        result = collection.update_many(query, {"$set": update_data})
        print(f"🔄 Updated {result.modified_count} documents in {collection_name}")

    def clear(self, collection_name: str):
        """Clear the specified collection."""
        collection = self.get_collection(collection_name)
        collection.delete_many({})
        print(f"🗑️ Cleared the collection: {collection_name}")

    def get_collection(self, collection_name: str):
        """Get a specific collection from the database."""
        return self.db[collection_name]
    
    def get_all_collections(self):
        """Get all collections in the database."""
        return self.db.list_collection_names()

    def is_duplicate(self, data: dict, collection_name: str) -> bool:
        """Check if data already exists by unique keys like guid or link."""
        collection = self.get_collection(collection_name)
        query = {"$or": []}

        # Check for unique fields like "guid" or "link"
        if "guid" in data:
            query["$or"].append({"guid": data["guid"]})
        if "link" in data:
            query["$or"].append({"link": data["link"]})

        if not query["$or"]:
            return False
        
        return collection.find_one(query) is not None
