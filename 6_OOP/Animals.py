from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass


class Cat(Animals):
    def voice(self):
        return "Meow"


cat = Cat()
print(cat.voice())
