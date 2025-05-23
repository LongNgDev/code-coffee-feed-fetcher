from fetcher.news_fetcher import NewsFetcher
from config.sources import sources

def main():
    try:
        
        print("📡 Starting to fetch feeds from configured sources...")
        fetcher = NewsFetcher(sources)
        fetcher.fetch()
       
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()

