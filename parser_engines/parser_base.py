

from abc import ABC, abstractmethod


class ArticleParser(ABC):
    @abstractmethod
    def parse(self, url:str) -> str:
        pass