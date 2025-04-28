# news_grouper.py

from difflib import SequenceMatcher

class NewsGrouper:
    def __init__(self, similarity_threshold: float = 0.6):
        self.similarity_threshold = similarity_threshold
        self.groups = []

    def similar(self, title1: str, title2: str) -> float:
        """Return similarity ratio between two titles."""
        return SequenceMatcher(None, title1.lower(), title2.lower()).ratio()

    def add_article(self, article: dict):
        """Add an article and group it into clusters."""
        for group in self.groups:
            if self.similar(group["representative_title"], article["title"]) >= self.similarity_threshold:
                group["articles"].append(article)
                return
        
        # If no similar group found, create a new group
        new_group = {
            "representative_title": article["title"],
            "articles": [article],
        }
        self.groups.append(new_group)

    def group_articles(self, articles: list[dict]):
        """Bulk grouping of articles."""
        for article in articles:
            self.add_article(article)

        return self.groups
