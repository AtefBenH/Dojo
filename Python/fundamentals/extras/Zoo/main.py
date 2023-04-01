from classes.zoo import Zoo

# animal = Animal ("Wolfo", 1, 15, 25)
# animal.display_info().eat().display_info()
zoo1 = Zoo("San Diego's Zoo").add_lion("Nala").add_lion("Simba").add_tiger("Rajah").add_tiger(
    "Shere Khan").add_bear("Baloo").add_bear("Mishka").print_all_info().feed_all().print_all_info()
