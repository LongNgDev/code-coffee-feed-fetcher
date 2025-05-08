# extractor/contentExtractor.py

import requests
from bs4 import BeautifulSoup as bs


class ContentExtractor:
    def __init__(self, link):
        self.link = link
        self.content = None

    def fetch_html(self):
        try:
            response = requests.get(self.link, timeout=10)
            response.raise_for_status()
            return bs(response.text, 'html.parser')
        except Exception as e:
            print(f"❌ Fetch error: {e}")
            return None

    def extract_content(self):
        raise NotImplementedError("You must implement extract_content in subclasses.")

    def get_content(self):
        return self.content
