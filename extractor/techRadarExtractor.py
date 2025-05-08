# extractor/techradar_extractor.py

import re
from bs4 import BeautifulSoup as bs
from extractor.contentExtractor import ContentExtractor


class TechRadarExtractor(ContentExtractor):
    def __init__(self, link, article: dict):
        super().__init__(link)
        self.raw_content = article.get("dc_content", None)

    def extract_content(self):
        if not self.raw_content:
            print("⚠️ No RSS content provided.")
            return None

        # Clean up CDATA wrapper if present
        html = self.raw_content.replace("<![CDATA[", "").replace("]]>", "").strip()
        soup = bs(html, "html.parser")

        # 💣 Remove irrelevant noise tags
        for tag in soup(["figure", "script", "style", "hr", "figcaption", "div"]):
            tag.decompose()

        # 🌸 Unwrap <a> but keep their inner text
        for a in soup.find_all("a"):
            a.unwrap()

        # ✨ Grab meaningful tags
        parts = []
        for tag in soup.find_all(["p", "h2", "h3", "li"]):
            text = tag.get_text(separator=' ', strip=True)
            if text:
                parts.append(text)

        raw_text = "\n\n".join(parts)

        # 🧹 Extra cleanup for text issues
        text = self._post_clean(raw_text)
        self.content = text
        return self.content

    def _post_clean(self, text: str) -> str:
        # Fix spacing issues between CamelCase or joined words
        text = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)  # e.g., AndorSeason → Andor Season
        text = re.sub(r'(?<=[a-zA-Z])(?=\d)', ' ', text)  # e.g., May7 → May 7
        text = re.sub(r'(?<=\d)(?=[A-Za-z])', ' ', text)  # e.g., 2024is → 2024 is

        # Remove weird line joins and fix punctuation spacing
        text = re.sub(r'\n{2,}', '\n\n', text)  # Keep double newlines only
        text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # Single newlines → space
        text = re.sub(r'\s+([.,!?])', r'\1', text)

        # Optional custom fixes for known edge cases
        known_fixes = {
            "notthebest": "not the best",
            "Andorseason": "Andor season",
            "spoiler-freereview": "spoiler-free review",
            "Disney+for": "Disney+ for",
            "StarWars": "Star Wars",
        }
        for broken, fixed in known_fixes.items():
            text = text.replace(broken, fixed)

        return text.strip()
