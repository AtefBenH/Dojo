from classes.dllist import DLList

dllist = DLList()
dllist.add_to_back(1).add_to_back(2).add_to_back(3).add_to_back(4).add_to_back(5).add_to_back(6).print_values()
print(f"List's length : {dllist.len}")
dllist.insert_value_at(0, 0).insert_value_at("Zéro", 0).insert_value_at("First", 1).insert_value_at("Third", 3).print_values()
print(f"List's length : {dllist.len}")
dllist.insert_value_at("Last Element",10).print_values()
print(f"List's length : {dllist.len}")
# dllist.delete_node(0).delete_node("First").print_values()
