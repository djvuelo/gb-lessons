from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @Clothes.fabric_consumption.getter
    def fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @Clothes.fabric_consumption.getter
    def fabric_consumption(self):
        return 2 * self.h + 0.3


coat1 = Coat(100)
costume1 = Costume(200)
print(coat1.fabric_consumption)
print(costume1.fabric_consumption)
