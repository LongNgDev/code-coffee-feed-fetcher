
from articles.Article import Article

class BlogArticle(Article):
    def __init__(self, title: str = "", author: str = "", content: str = "", sources: list[str] = []):
        super().__init__(title, author, content)
        self.sources = sources

    """ Setters """
    
    def set_sources(self, sources: list[str]):
        self.sources = sources

    """ Getters """

    def get_sources(self):
        return self.sources
    
    """ Other methods """
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "content": self.content,
            "sources": self.sources
        }
