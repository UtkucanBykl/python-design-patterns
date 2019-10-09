class XMLCrawler:
    def crawle(self):
        return 'Crawle with XML'

class Adapter:
    _xml_crawler = None

    def __init__(self, xml_crawler):
        self._xml_crawler = xml_crawler

    def convertJson(self, value):
        return 'Convert Json ' + str(value)

class Crawler:
    _adapter = None
    
    def __init__(self, adapter):
        self._adapter = adapter

    def crawle(self):
        return self._adapter.convertJson(self._adapter._xml_crawler.crawle())

xml_crawler = XMLCrawler()
adapter = Adapter(xml_crawler)
crawle = Crawler(adapter)

print(crawle.crawle())

