# mongodb_storage.py

from storage.mongo_client import MongoDBClient
from datetime import datetime, timezone

class NewsSaver:
    def __init__(self, client: MongoDBClient, collection_name: str = "news_articles"):
        self.collection = client.get_collection(collection_name)

    def save_articles(self, articles: list[dict]):
        """Save list of articles to MongoDB with duplicate check."""

        if not articles:
            print("⚠️ No articles to save.")
            return
        
        for article in articles:
            article = article.to_dict()
            # Check if article is already in the database
            if self.is_duplicate(article):
                continue

            article["saved_at"] = datetime.now(timezone.utc)
            self.collection.insert_one(article)
            print(f"✅ Saved article: {article['title']}")

    def is_duplicate(self, article: dict) -> bool:
        """Check if article already exists by guid or link."""
        query = {"$or": []}
        if "guid" in article:
            query["$or"].append({"guid": article["guid"]})
        if "link" in article:
            query["$or"].append({"link": article["link"]})

        if not query["$or"]:
            return False
        
        return self.collection.find_one(query) is not None
    
    def clear_collection(self):
        """Clear the collection."""
        self.collection.delete_many({})
        print("🗑️ Cleared the collection.")