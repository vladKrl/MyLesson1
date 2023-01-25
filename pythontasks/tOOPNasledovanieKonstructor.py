class Animal:
    def __init__(self, kind, habitat):
        self.kind = kind
        self.habitat = habitat

    def habitatAnimal(self):
        print(self.kind + " is from " + self.habitat)

    def size(self, height, width):
        print(self.kind + " is", height, "meters high and", width, "meters wide")

    def amountOfAnimals(self, amount):
        print("There are", amount, self.kind + " in the world")

class MythicalAnimal(Animal):
    def __init__(self, kind, habitat, work):
        super().__init__(kind, habitat)
        self.work = work

    def _amountOfAnimals(self, amount):
        print("There are 0 " + self.kind + " in the world because it's a mythical animal.")

    def composition(self):
        print(self.kind + " is show up in the " + self.work)

class ExtinctAnimal(Animal):
    def __init__(self, kind, habitat, extinctionMil):
        super().__init__(kind, habitat)
        self.extinctionMil = extinctionMil

    def _amountOfAnimals(self, amount):
        print("There are 0 " + self.kind + " in the world because it's an extinct animal.")

    def whenExtinct(self):
        print(self.kind + " became extinct", self.extinctionMil, "millions years ago.")

class ArtificialAnimal(Animal):
    _status = "Artificial"

    def __init__(self, kind, habitat, creator):
        super().__init__(kind, habitat)
        self.creator = creator

    def _amountOfAnimals(self, amount):
        print("There are", amount, self.kind + " created in the world")

    def __creatorAnimal(self):
        print(self.kind + " was created by " + self.creator + ".")

an1 = ArtificialAnimal("BigDog", "Laboratory", "Boston Dynamics")

an1.habitatAnimal()
an1.size(2, 3)
an1._amountOfAnimals(1002)
an1._ArtificialAnimal__creatorAnimal()

print("Статус существа " + an1.kind + " - " + an1._status)