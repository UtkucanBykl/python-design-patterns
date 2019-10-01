from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def pixel(self):
        pass

class MobileGame(Game):
    def pixel(self):
        return '720x1080'

class Adapter:
    _mobile_game = None
    _pixel_translate = {
        '720x1080': '1080:2040'
    }

    def __init__(self, mobil_game):
        self._mobile_game = mobil_game

class PCGame(Game):
    _adapter = None

    def __init__(self, adapter):
        self._adapter = adapter

    def pixel(self):
        return self._adapter._pixel_translate[self._adapter._mobile_game.pixel()]


mobil_game = MobileGame()
adapter = Adapter(mobil_game)
pc_game = PCGame(adapter)

print(pc_game.pixel())
