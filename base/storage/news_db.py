from base.storage.mongodb_client import MongoDBClient
from datetime import datetime, timezone


class NewsDB(MongoDBClient):
    def __init__(self, uri: str = "mongodb://127.0.0.1:27017/", db_name: str = "code_and_coffee_db", collection_name: str = "news_articles"):
        super().__init__(collection_name)
        self.collection_name = collection_name

    def save_article(self, article: dict):
        """Save a single news article with timestamp."""
        if "saved_at" not in article:
            article["saved_at"] = datetime.now(timezone.utc)
        self.save(article)

    def fetch_articles(self, query: dict):
        """Fetch news articles from the database."""
        return self.fetch(query)

    def update_article(self, query: dict, update_data: dict):
        """Update news articles in the database."""
        self.update(query, update_data )

    def delete_articles(self, query: dict):
        """Delete news articles from the database."""
        self.delete(query )

    def clear_news(self):
        """Clear the news collection."""
        self.clear()

    def list_articles(self):
        """List all articles in the news collection."""
        return self.fetch({}, )

    def is_duplicate_article(self, article: dict) -> bool:
        """Check if an article is a duplicate."""
        return self.is_duplicate(article)
