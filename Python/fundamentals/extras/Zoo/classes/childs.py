from classes.animal import Animal
class Lion (Animal) :
    def __init__(self, name, age=0, health=10, happiness=5, meat_amount=5):
        super().__init__(name, age, health, happiness)
        self.meat_amount = meat_amount

    def eat(self):
        self.health+=15
        self.happiness+=15
        return self

class Tiger (Animal) :
    def __init__(self, name, age=0, health=20, happiness=15, origin="Africa"):
        super().__init__(name, age, health, happiness)
        self.origin = origin

    def eat(self):
        self.health+=5
        self.happiness+=10
        return self

class Bear (Animal) :
    def __init__(self, name, age=0, health=15, happiness=10, isPolar=False):
        super().__init__(name, age, health, happiness)
        self.isPolar = isPolar

    def eat(self):
        self.health+=10
        self.happiness+=5
        return self

