from abc import ABC, abstractmethod


class Crawler(ABC):
    def __init__(self):
        self._observers = []
        self._url = 'http://www.koeri.boun.edu.tr/scripts/lst7.asp'

    @abstractmethod
    def crawle(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        return [observer.update(self) for observer in self._observers]

class QuakeCrawler(Crawler):
    def crawle(self):
        print('aaa')

    def parse(self):
        print('bbb')

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class TelegramBot(Observer):
    def update(self, observer):
        print('Send telegram message about {}'.format(observer._url))

qcrawler = QuakeCrawler()
telegram_bot = TelegramBot()
qcrawler.add(telegram_bot)
qcrawler.crawle()
qcrawler.notify()

