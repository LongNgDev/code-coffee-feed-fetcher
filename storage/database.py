# mongodb_storage.py

from pymongo import MongoClient
from datetime import datetime

class MongoDBNewsStorage:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="code_and_coffee_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["news_groups"]

    def save_group(self, group: dict):
        """Save a news group if not duplicate."""
        if not group.get("articles"):
            return  # Ignore empty groups

        representative_title = group.get("representative_title", "")
        first_article = group["articles"][0]
        guid = first_article.get("guid")
        link = first_article.get("link")

        if self.is_duplicate(guid, link):
            print(f"⚠️ Duplicate group found. Skipping: {representative_title}")
            return

        group["date_saved"] = datetime.utcnow().isoformat()
        self.collection.insert_one(group)

    def is_duplicate(self, guid: str, link: str) -> bool:
        """Check if an article already exists by guid or link."""
        query = {"$or": []}
        if guid:
            query["$or"].append({"articles.guid": guid})
        if link:
            query["$or"].append({"articles.link": link})

        if not query["$or"]:
            return False  # No valid id to check

        return self.collection.find_one(query) is not None

    def clear_db(self):
        """Clear all records (careful!)"""
        self.collection.delete_many({})

    def fetch_all_groups(self):
        """Fetch all saved groups."""
        return list(self.collection.find({}))
