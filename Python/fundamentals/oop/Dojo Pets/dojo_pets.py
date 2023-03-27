from ninja import Ninja
from pet import *

#Main
treats = ["Green Peas", "Carrots", "Bananas", "Green Beans", "Broccoli"]
pet_food = ["Eggs", "Peanuts", "Blueberries", "Celery", "Peaches"]

# fish = Pet("Pepsi","Fish",['jumps high','sings'], "Plouf Plouf")
rabbit = Herbivore("Pepsi","Rabbit",['jumps high','sings'], "New York New Yoooork")
naruto = Ninja("Naruto","Uzumaki", rabbit, treats, pet_food)
naruto.check_pet()
naruto.walk()
naruto.feed()
naruto.bathe()
naruto.check_pet()

cat = Carnivorous("MrBonkers", "Cat", ['flies','sleeps a lot'], "Miaou Miaou")
sasuke = Ninja("Sasuke","Uchiha", cat, treats, pet_food)
sasuke.check_pet()
sasuke.feed()
sasuke.walk()
sasuke.bathe()
sasuke.check_pet()

