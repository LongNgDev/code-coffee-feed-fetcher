# extractor/techcrunch_extractor.py

from fetcher.extractor.contentExtractor import ContentExtractor


class TechCrunchExtractor(ContentExtractor):
    def __init__(self, link):
        super().__init__(link)
        self.content = None

    def extract_content(self):
        soup = self.fetch_html()
        if not soup:
            return None

        article_div = soup.find("div", class_="entry-content")
        if not article_div:
            print("⚠️ Could not find article content.")
            return None

        paragraphs = article_div.find_all("p", class_="wp-block-paragraph")
        cleaned = [
            ' '.join(p.stripped_strings)
            for p in paragraphs if p.get_text(strip=True)
        ]
        self.content = "\n\n".join(cleaned)
        return self.content
