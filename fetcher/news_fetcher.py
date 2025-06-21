from urllib.parse import urlparse
from fetcher.fetcher import Fetcher
from base.articles.newsArticle import NewsArticle
from fetcher.extractor.factory import get_extractor_for_url

from generator.slugGenerator import SlugGenerator
from generator.contentGenerator import ContentGenerator

from base.extractor.tagsExtractor import TagsExtractor
from base.extractor.thumbnailExtractor import ThumbnailExtractor
from base.storage.news_db import NewsDB

class NewsFetcher(Fetcher):
    def __init__(self, sources: list[dict]):
        super().__init__(sources)
        self.db = NewsDB()

    def fetch(self):
        try:
            """Fetch feeds with extra logging ✨"""
            print("📡 Starting to fetch feeds from", len(self.sources), "sources!")

            # Fetch the articles from the sources
            super().fetch()  # Reuse parent's fetch method

            print("✅ Done fetching! Got", len(self.articles), "articles total.")

            articles = self.get_articles()

            # Initialize the database connection
            print(f"🗄️ Saving {len(articles)} articles to the database...")

            # Save each article to the database
            for article in articles:
                self.db.save_article(article.to_dict())
            
            print("🎉 All articles processed successfully.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        finally:
            # Close the database connection
            self.db.disconnect()
            print("🛑 Database connection closed.")

    def get_articles(self):
        """Return the list of fetched articles."""
        articles = []
        contentGenerator = ContentGenerator(model_name="mistral")

        for entry in self.articles:

            # Check if the article is duplicated
            if self.db.is_duplicate_article(entry):
                # print(f"The article is duplicated!")
                continue
            
            link = getattr(entry, "link", "") 
            
            # Check if the link is a video link and skip it
            parsed_link = urlparse(link)
            # Check if the path contains "video"
            is_video = parsed_link.path.split("/")[1] == "video"

            if is_video:
                print(f"Skipping video link: {link}")
                continue

            title = getattr(entry, "title", None)
            published = getattr(entry, "published", None)
            summary = getattr(entry, "summary", getattr(entry, "description", ""))
            guid = getattr(entry, "id", None) 
            authors = getattr(entry, "author", None)

            extractor = get_extractor_for_url(link)

            raw_content = extractor.extract_content()
            ai_content = contentGenerator.generate_content(raw_content) 

            with TagsExtractor() as tags_extractor:
                tags = tags_extractor.extract_tags(raw_content)

            slugGenerator = SlugGenerator(title)
            slugGenerator.generate_slug()
            slug = slugGenerator.get_slug()

            # Extract thumbnail
            # thumbnailExtractor = ThumbnailExtractor()
            thumbnail = slug
            

            # Create the article object
            article = NewsArticle(title=title, link=link, authors=authors, published=published, summary=summary, guid=guid, tags=tags, raw_content=raw_content, ai_content=ai_content, slug=slug, thumbnail=thumbnail)

            articles.append(article)    

        return articles
