from abc import ABC, abstractmethod

class User:
    def __init__(self, name):
        self.name = name


class IUserIterator(ABC):
    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

class UserIterator(IUserIterator):
    def __init__(self, user_aggregate):
        self._index = 0
        self._user_aggregate = user_aggregate

    def is_done(self):
        return self._index >= self._user_aggregate.count

    def current(self):
        return self._user_aggregate.users[self._index]

    def next(self):
        self._index += 1
        if not self.is_done():
            return self._user_aggregate.users[self._index]
        raise IndexError('Last item')


class UserAggregate:
    def __init__(self):
        self.users = list()

    def add(self, user):
        self.users.append(user)

    def remove(self, index):
        self.users.remove(index)

    def user_iterator(self):
        return UserIterator(self)

    @property
    def count(self):
        return len(self.users)

    @count.setter
    def count(self):
        raise BaseException('Only get')

utku = User('utku')
ahmet = User('ahmet')
mehmet = User('mehmet')
user_aggregate = UserAggregate()
user_iterator = user_aggregate.user_iterator()
user_aggregate.add(utku)
user_aggregate.add(ahmet)
user_aggregate.add(mehmet)
print(user_iterator.current().name)
print(user_iterator.next().name)
print(user_iterator.next().name)
print(user_iterator.next().name)
