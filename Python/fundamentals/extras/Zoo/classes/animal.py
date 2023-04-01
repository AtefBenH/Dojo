class Animal :
    def __init__(self, name, age=0, health=0, happiness=0) :
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    
    def eat(self) :
        self.health+=10
        self.happiness+=10
        return self

    def display_info(self) :
        print(f"Name : {self.name} -- Age : {self.age} -- Health : {self.health} -- Happiness : {self.happiness}")
        return self
    