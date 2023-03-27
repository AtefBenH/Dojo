class Ninja :
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self) :
        self.pet.play()
        # print("Walked")
        return self
    
    def feed (self) :
        self.pet.eat()
        # print("ate")
        return self
    
    def bathe(self) :
        # print("cleaned")
        self.pet.noise()
    
    def check_pet(self):
        self.pet.display_health_energy()