

from urllib.parse import urlparse
from parser_engines.techcrunch_parser import TechCrunchParser
from parser_engines.parser_base import ArticleParser

PARSER_MAP: dict[str, ArticleParser] = {
    "techcrunch.com": TechCrunchParser(),
    # "theverge.com": TheVergeParser(),
    # ...
}

class ParserManager():
    """ This class help controlling the traffic of deciding using which parser for each certain known domain. """
    def get_parser(self, url: str) -> ArticleParser:
        # Extract the domain using urlparse with netloc
        domain = urlparse(url).netloc.replace("www", "")
        return PARSER_MAP.get(domain)