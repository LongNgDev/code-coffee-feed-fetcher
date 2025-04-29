# main.py

from fetcher.rss_fetcher import FeedFetcher
from grouper.news_grouper import NewsGrouper
from config.sources import sources

def main():
    fetcher = FeedFetcher(sources)
    articles = fetcher.fetch_all()

    print(f"\n🔵 Fetched {len(articles)} articles!")

if __name__ == "__main__":
    main()
