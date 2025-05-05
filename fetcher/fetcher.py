import feedparser
from articles.articleClass import Article
import json


class Fetcher:
  def __init__(self, sources: list[dict]):
    self.sources = sources
    self.articles = []

  def fetch(self):
    """Fetch all feeds and store list of articles."""
    for source_info in self.sources:
      source_url = source_info["url"]
      feed = feedparser.parse(source_url)
      self.articles.extend(feed.entries)  # flattening the list


  def get_articles(self):
    """Return the list of fetched articles."""
    articles = []

    for entry in self.articles:
      
      article = Article()

      title = getattr(entry, "title", None)
      link = getattr(entry, "link", None) 
      published = getattr(entry, "published", None)
      summary = getattr(entry, "summary", getattr(entry, "description", ""))
      guid = getattr(entry, "id", None) 
      authors = getattr(entry, "author", None) 

      article.set_title(title)
      article.set_link(link)
      article.set_author(authors)
      article.set_published(published)
      article.set_summary(summary)
      article.set_guid(guid)

      articles.append(article)    
    return articles

