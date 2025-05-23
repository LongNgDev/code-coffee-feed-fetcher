

class Article:
    def __init__(self, title, authors, content):
        self.title = title
        self.authors = authors
        self.content = content

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Content: {self.content}"
    
    def __dict__(self):
        return {
            "title": self.title,
            "author": self.author,
            "content": self.content
        }
    
    """ Setters """
    def set_title(self, title: str):
        self.title = title

    def set_authors(self, authors: str):
        self.authors = authors

    def set_content(self, content: str):
        self.content = content

    """ Getters """
    def get_title(self):
        return self.title
    
    def get_authors(self):
        return self.authors
    
    def get_content(self):
        return self.content
    
    """ Methods """
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "content": self.content
        }