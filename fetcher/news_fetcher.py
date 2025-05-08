from fetcher.fetcher import Fetcher
from articles.articleClass import Article
from extractor.factory import get_extractor_for_url
import json

from generator.aiClient import AiClient

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

        for entry in self.articles:

            title = getattr(entry, "title", None)
            link = getattr(entry, "link", "") 
            published = getattr(entry, "published", None)
            summary = getattr(entry, "summary", getattr(entry, "description", ""))
            guid = getattr(entry, "id", None) 
            authors = getattr(entry, "author", None)
            
            extractor = get_extractor_for_url(link)
            content = extractor.extract_content()

            client = AiClient(model_name="llama3")
            prompt = f"""
            Extract only the most relevant, concise keywords or tags that best describe the content of the following tech-focused article. Focus on technology-related terms, industry keywords, and company names. Return the tags as a single, comma-separated list with no explanations, no formatting, and no introductory text. 

            Article:
            {content}

            Output:
            [list of tags]
            """

            
            # Generate tags and ensure they are a list
            raw_tags = client.generate(prompt)

            # Split and clean tags
            tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
            print(f"Tags for {title}: {tags}")
            client.close()

            # Create the article object
            article = Article()

            article.set_title(title)
            article.set_link(link)
            article.set_author(authors)
            article.set_published(published)
            article.set_summary(summary)
            article.set_guid(guid)
            # article.set_content(content)
            article.set_tags(tags)

            articles.append(article)    

        return articles
