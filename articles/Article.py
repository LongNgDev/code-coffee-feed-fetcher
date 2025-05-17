

class Article:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
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

    def set_author(self, author: str):
        self.author = author

    def set_content(self, content: str):
        self.content = content

    """ Getters """
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_content(self):
        return self.content
    
    """ Methods """
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "content": self.content
        }