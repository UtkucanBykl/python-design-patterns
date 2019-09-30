from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Hav'


class Cat(Animal):
    def speak(self):
        return 'Miv'


class AnimalFactory:
    def get_factory(self, name):
        if name == 'Dog':
            return Dog()
        elif name == 'Cat':
            return Cat()

    def create_animal(self, name, kind):
        factory_class = self.get_factory(kind)
        print(factory_class.speak())

a = AnimalFactory()
a.create_animal('Hello', 'Dog')
