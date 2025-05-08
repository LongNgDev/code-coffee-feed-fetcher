from abc import ABC
from storage.db_interface import DatabaseInterface


class BaseDatabase(DatabaseInterface, ABC):
    def __init__(self, client, db_name: str):
        self.client = client
        self.db_name = db_name
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        """Get a specific collection from the database."""
        return self.db[collection_name]

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

    def clear_collection(self, collection_name: str):
        """Clear the specified collection."""
        collection = self.get_collection(collection_name)
        collection.delete_many({})
        print(f"🗑️ Cleared the collection: {collection_name}")
