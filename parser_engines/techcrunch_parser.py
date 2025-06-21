

from bs4 import BeautifulSoup as bs
from parser_engines.parser_base import ArticleParser
import requests


class TechCrunchParser(ArticleParser):
  def __init__(self, url: str = ""):
    self.url = url

  def parse(self, url: str = None) -> str:
    if url:
      self.url = url

    # Fetch the data from source url
    response = requests.get(self.url)

    # Parse the response into html format
    soup = bs(response.text, "html.parser")
    # Find the main content area
    main = soup.find("div", class_="entry-content")

    # Pull out all the <p> tags that contain main content
    content_frags = main.findAll("p", class_="wp-block-paragraph")

    # Combine and trim the list into a article
    content = self.__combine_content(content_frags)

    return content
  
  # Helper: clean and combine text from list to article
  def __combine_content(self, raw_inputs: list[str]) -> str:
    if len(raw_inputs) == 0:
      return
    
    cleaned_content = "\n".join(p.get_text(strip=True) for p in raw_inputs)

    return cleaned_content