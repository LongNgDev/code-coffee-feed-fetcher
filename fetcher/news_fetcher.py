import feedparser
import json
from fetcher.fetcher import Fetcher

class NewsFetcher(Fetcher):
    def __init__(self, sources: list[dict]):
        super().__init__(sources)

    def fetch(self):
        """Fetch feeds with extra logging ✨"""
        print("📡 Starting to fetch feeds from", len(self.sources), "sources!")
        super().fetch()  # Reuse parent's fetch method
        print("✅ Done fetching! Got", len(self.articles), "articles total.")