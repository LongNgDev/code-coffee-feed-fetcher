from fetcher.fetcher import Fetcher
from articles.articleClass import Article
from extractor.contentExtractor import ContentExtractor
from extractor.factory import get_extractor_for_url
import json

class NewsFetcher(Fetcher):
    def __init__(self, sources: list[dict]):
        super().__init__(sources)

    def fetch(self):
        """Fetch feeds with extra logging ✨"""
        print("📡 Starting to fetch feeds from", len(self.sources), "sources!")
        super().fetch()  # Reuse parent's fetch method
        print("✅ Done fetching! Got", len(self.articles), "articles total.")

    def get_articles(self):
        """Return the list of fetched articles."""
        articles = []

        for entry, source_url  in self.articles:
        
            title = getattr(entry, "title", None)
            link = getattr(entry, "link", None) 
            published = getattr(entry, "published", None)
            summary = getattr(entry, "summary", getattr(entry, "description", ""))
            guid = getattr(entry, "id", None) 
            authors = getattr(entry, "author", None)

            extractor = get_extractor_for_url(link)
            # extractor = get_extractor_for_url(link, entry)
            content = extractor.extract_content()

            article = Article()

            article.set_title(title)
            article.set_link(link)
            article.set_author(authors)
            article.set_published(published)
            article.set_summary(summary)
            article.set_guid(guid)
            article.set_content(content)

            articles.append(article)    

        return articles