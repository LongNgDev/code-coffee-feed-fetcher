from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri: str = "mongodb://localhost:27017/", db_name: str = "code_and_coffee_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        """Get a collection from the database."""
        return self.db[collection_name]