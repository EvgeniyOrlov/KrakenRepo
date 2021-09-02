from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return (2 * self.size + 0.3) / 100


coat_size = Coat(50)
suit_size = Suit(176)

print(f'Расход ткани на пальто: {coat_size.consumption:.3f} см.')
print(f'Расход ткани на костюм: {suit_size.consumption:.3f} см.')
print(f'Общий расход ткани: {coat_size.consumption + suit_size.consumption:.3f} см.')
