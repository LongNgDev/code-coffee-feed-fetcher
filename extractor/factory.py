# extractor/factory.py

from urllib.parse import urlparse
from extractor.techCrunchExtractor import TechCrunchExtractor
from extractor.techRadarExtractor import TechRadarExtractor

def get_extractor_for_url(link, article: dict = None):
    domain = urlparse(link).netloc

    if "techcrunch.com" in domain:
        return TechCrunchExtractor(link)
    """elif "techradar.com" in domain:
        return TechRadarExtractor(link, article) """
    
    
    # fallback or more mappings later
    raise ValueError(f"No extractor available for domain: {domain}")
