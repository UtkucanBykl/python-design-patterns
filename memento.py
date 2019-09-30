from abc import ABC, abstractmethod

class Setting:

    def __init__(self):
        self._name = ''
        self._status = False
        self._age = -1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status



    def save(self):
        return Memento(self._name, self._age, self._status)

    def restore(self, memento):
        self._name = memento.name
        self.age = memento.age
        self.status = memento.status


class Memento:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status


class Memory:

    def __init__(self):
        self.memory_memento = []

    @property
    def memento(self):
        if self.memory_memento:
            return self.memory_memento.pop()

    @memento.setter
    def memento(self, memory_memento):
        self.memory_memento.append(memory_memento)

    def history(self):
        for m in self.memory_memento:
            yield m


s = Setting()
m = Memory()
s.name = 'Ahmet'
s.status = True
s.age = 15
m.memory_memento = s.save()
s.name = 'Mehmet'
m.memory_memento = s.save()
s.name = 'Ali'
print(list(m.history()))

s.restore(m.memory_memento)
s.restore(m.memory_memento)
print(s.name)
