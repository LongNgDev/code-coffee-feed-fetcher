from fetcher.news_fetcher import NewsFetcher
from config.sources import sources
from storage.mongo_client import MongoDBClient
from storage.news_saver import NewsSaver

def main():
    # 🔍 Step 1: Fetch articles
    fetcher = NewsFetcher(sources)
    fetcher.fetch()
    articles = fetcher.get_articles()

    # Print the number of articles fetched
    print(f"Fetched {len(articles)} articles.")

    # 💾 Step 2: Save to MongoDB
    client = MongoDBClient()
    saver = NewsSaver(client)
    saver.clear_collection()  # Optional: Clear the collection before saving new articles
    saver.save_articles(articles)

if __name__ == "__main__":
    main()
