from fetcher.news_fetcher import NewsFetcher
from config.sources import sources
from storage.news_db import NewsDB

def main():
    try:
        # 📡 Step 1: Fetch articles
        print("📡 Starting to fetch feeds from configured sources...")
        fetcher = NewsFetcher(sources)
        fetcher.fetch()
        articles = fetcher.get_articles()

        # Print the number of articles fetched
        # print(f"✅ Done fetching! Got {len(articles)} articles total.")

        # 💾 Step 2: Save to MongoDB
        db = NewsDB()
        print(f"🗄️ Saving {len(articles)} articles to the database...")

        # Optional: Clear the collection before saving new articles
        db.clear_news()

        for article in articles:
            
            db.save_article(article.to_dict())

        print("🎉 All articles saved successfully.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        # Close the database connection
        db.disconnect()
        print("🛑 Database connection closed.")

if __name__ == "__main__":
    main()
