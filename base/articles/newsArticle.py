


from base.articles.Article import Article


class NewsArticle(Article):
    def __init__(self, title: str = "", link: str = "", authors: str = "", published: str = "", summary: str = "", guid: str = "", tags: list[str] = [""], raw_content: str = "", ai_content: str = "", slug: str = "", thumbnail: str = ""):
        super().__init__(title, authors, raw_content)
        self.link = link
        self.published = published
        self.summary = summary
        self.tags = tags
        self.guid = guid
        self.slug = slug
        self.ai_content = ai_content
        self.thumbnail = thumbnail

    """ Setters """ 
    
    def set_link(self, link: str):
        self.link = link
    
    def set_published(self, published: str):
        self.published = published

    def set_summary(self, summary: str):
        self.summary = summary

    def set_guid(self, guid: str):
        self.guid = guid

    def set_tags(self, tags: list[str]):
        self.tags = tags

    def set_slug(self, slug: str):
        self.slug = slug

    def set_ai_content(self, ai_content: str):
        self.ai_content = ai_content

    def set_thumbnail(self, thumbnail: str):
        self.thumbnail = thumbnail

    """ Getters """
    def get_link(self):
        return self.link
    
    def get_published(self):
        return self.published
    
    def get_summary(self):
        return self.summary
    
    def get_guid(self):
        return self.guid
    
    def get_tags(self):
        return self.tags
    
    def get_slug(self):
        return self.slug
    
    def get_ai_content(self):
        return self.ai_content

    def get_thumbnail(self):
        return self.thumbnail

    """ Other methods """

    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "slug": self.slug,
            "raw_content": self.content,
            "ai_content": self.ai_content,
            "tags": self.tags,
            "authors": self.authors,
            "published": self.published,
            "summary": self.summary,
            "guid": self.guid,
            "thumbnail": self.thumbnail,
        }
        
        
        