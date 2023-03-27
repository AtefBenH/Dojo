import abc
class Pet :
    def __init__(self, name , type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.sound = sound

    @abc.abstractmethod
    def sleep (self) :
        raise NotImplementedError
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound)

    def display_health_energy(self):
        print (f"Name : {self.name}, Health : {self.health}, Energy : {self.energy}")

class Carnivorous (Pet) :
    def __init__(self, name, type, tricks, sound) :
        super().__init__(name, type, tricks, sound)

    def sleep (self) :
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 15
        self.health += 5
        return self

class Herbivore (Pet) :
    def __init__(self, name, type, tricks, sound) :
        super().__init__(name, type, tricks, sound)

    def sleep (self) :
        self.energy += 50
        return self
    
    def eat(self):
        self.energy += 10
        self.health += 15
        return self
