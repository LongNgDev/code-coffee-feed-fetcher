# main.py

from fetcher.rss_fetcher import FeedFetcher
from grouper.news_grouper import NewsGrouper
from config.sources import sources

def main():
    fetcher = FeedFetcher(sources)
    articles = fetcher.fetch_all()

    print(f"\n🔵 Fetched {len(articles)} articles!")

    # Start Grouper
    """ grouper = NewsGrouper(similarity_threshold=0.8)
    groups = grouper.group_articles(articles)

    print(f"\n🧠 Grouped into {len(groups)} topic clusters!")

    for i, group in enumerate(groups[:5], 1):  # preview first 5 clusters
      print(f"\n🗂️ Group {i}:")
      print(f"🔖 Representative Title: {group['representative_title']}")
      print(f"🧩 Articles in this group:")

      for j, article in enumerate(group["articles"], 1):
          print(f"  {j}. 📰 Title: {article['title']}")
          print(f"     🔗 Link: {article['link']}")
          print(f"     🏷️ Source: {article.get('source_url', 'Unknown Source')}")
          print(f"     🕒 Published: {article.get('published', 'No Date')}")
          print() """


if __name__ == "__main__":
    main()
