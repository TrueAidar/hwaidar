from abc import ABC, abstractmethod

class FarmAnimal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def go_to_farm(self):
        pass


class Farmer(FarmAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.animals_to_gather = []

    def add_animals(self):
        self.animals_to_gather.append(self.name)

    def go_to_farm(self):
        return f'Go to farm {self.name}!'

class Pig(Farmer):
    pass

class Dog(Farmer):
    pass

class Sheep(Farmer):
    pass

class Horse(Farmer):
    pass


pig = Pig('Pig')
dog = Dog('Dog')
sheep = Sheep('Sheep')
horse = Horse('Horse')
farmer = Farmer('Askar')
print('I am ' + farmer.name + ', your farmer!')
print(farmer.add_animals())
print(pig.go_to_farm())
print(dog.go_to_farm())
print(sheep.go_to_farm())
print(horse.go_to_farm())
