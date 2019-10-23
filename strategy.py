from abc import ABC, abstractmethod

class Crawle(ABC):
    @abstractmethod
    def get(self):
        pass


class CrawleJSON(Crawle):
    def get(self):
        print({'type': 'json'})


class CrawleXML(Crawle):
    def get(self):
        print('<xml></xml>')


class Context:
    def __init__(self):
        self.crawle = None

    @property
    def crawler(self):
        return self.crawle

    @crawler.setter
    def crawler(self, value):
        self.crawle = value

    def run(self):
        self.crawle.get()


if __name__ == "__main__":
    j_crawle = CrawleJSON()
    x_crawle = CrawleXML()
    context = Context()
    context.crawle = j_crawle
    context.run()
    context.crawle = x_crawle
    context.run()
