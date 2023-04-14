from classes.store import Store
from classes.product import Product

it_store = Store("Storetec")
smartphone = Product("Samsung S20", "Smatphone", 1500)
earbuds = Product("Xiaomi Mi True", "Earbuds", 150)
laptop1 = Product("Dell-XPS", "Laptop", 3000)
laptop2 = Product("Toshiba", "Laptop", 2500)
laptop3 = Product("IBM", "Laptop", 2800)
laptop4 = Product("MacBook", "Laptop", 5200)

print("Products in the store")
print("------------------------------------------------------------------")
it_store.add_product(smartphone).add_product(earbuds).add_product(laptop1).add_product(laptop2).add_product(laptop3).add_product(laptop4)
it_store.show_all_products()
print("------------------------------------------------------------------")
it_store.sell_product(2)
it_store.sell_product(5)
print("Products after price's updates and sells")
print("------------------------------------------------------------------")
it_store.show_all_products()
print("------------------------------------------------------------------")
# smartphone.update_price(.4, False)
# laptop1.update_price(.2, True)
# it_store.show_all_products()
# print("------------------------------------------------------------------")

# print("Prices after inflation")
# print("------------------------------------------------------------------")
# it_store.inflation(.5)
# it_store.show_all_products()
# print("------------------------------------------------------------------")

# print("Products in the store after clearence")
# print("------------------------------------------------------------------")
# it_store.set_clearance("Laptop", .2)
# it_store.show_all_products()
# print("------------------------------------------------------------------")

