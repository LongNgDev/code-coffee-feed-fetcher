class Article:
    def __init__(self, title: str = "", link: str = "", author: str = "", published: str = "", summary: str = "", guid: str = ""):
        self.title = title
        self.link = link
        self.author = author
        self.published = published
        self.summary = summary
        self.guid = guid

    def set_title(self, title: str):
        self.title = title
    
    def set_link(self, link: str):
        self.link = link
    
    def set_author(self, author: str):
        self.author = author
    
    def set_published(self, published: str):
        self.published = published

    def set_summary(self, summary: str):
        self.summary = summary

    def set_guid(self, guid: str):
        self.guid = guid

    def get_title(self):
        return self.title
    
    def get_link(self):
        return self.link
    
    def get_author(self):
        return self.author
    
    def get_published(self):
        return self.published
    
    def get_summary(self):
        return self.summary
    
    def get_guid(self):
        return self.guid
    
    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "author": self.author,
            "published": self.published,
            "summary": self.summary,
            "guid": self.guid
        }
        
        
        