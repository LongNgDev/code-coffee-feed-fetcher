import feedparser



class Fetcher:
  def __init__(self, sources: list[dict]):
    self.sources = sources
    self.articles = []

  def fetch(self):
    """Fetch all feeds and store list of articles."""
    for source_info in self.sources:
      source_url = source_info["url"]
      feed = feedparser.parse(source_url)

      self.articles.extend((entry, source_url) for entry in feed.entries)  # flattening the list


  def get_articles(self):
    raise NotImplementedError("This method should be implemented in subclasses")