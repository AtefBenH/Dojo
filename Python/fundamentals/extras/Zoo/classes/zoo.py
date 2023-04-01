from classes.childs import Lion, Tiger, Bear
from classes.animal import Animal
class Zoo :
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self
    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self
    def add_bear(self, name):
        self.animals.append(Bear(name))
        return self
    
    def feed_all(self):
        for animal in self.animals:
            animal.eat()
        return self

    def print_all_info(self):
        print("-"*30, self.zoo_name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self