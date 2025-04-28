import feedparser
import json

class FeedFetcher:
    def __init__(self, sources: list[dict]):
        self.sources = sources  # FIXED (use consistent naming)

    def fetch_all(self):
        """Fetch all feeds and return list of articles."""
        articles = []

        for source_info in self.sources:
            source_url = source_info["url"]
            priority = source_info["priority"]

            feed = feedparser.parse(source_url)
            
            print(f"Keys: {json.dumps(feed.entries[1], indent=2)}")
            # print(f"Values: {feed.entries[1].values()}")

            for entry in feed.entries:
                title = getattr(entry, "title", None) or "[No Title]"
                link = getattr(entry, "link", None) or ""
                published = getattr(entry, "published", None)
                summary = getattr(entry, "summary", getattr(entry, "description", "")) or "[No Summary]"
                guid = getattr(entry, "id", None) or "[No GUID]"
                authors = getattr(entry, "author", None) or "[No Author]"

                article = {
                    "guid": guid,
                    "title": title,
                    "link": link,
                    "author": authors,
                    "published": published,
                    "summary": summary,
                    "priority": priority,
                    "source_url": source_url
                }
                articles.append(article)

        return articles

    def fetch_by_priority(self, min_priority: int = 2) -> list[dict]:
        """Fetch articles only from sources with priority <= min_priority."""
        filtered_sources = [s for s in self.sources if s["priority"] <= min_priority]
        fetcher = FeedFetcher(filtered_sources)
        return fetcher.fetch_all()

    