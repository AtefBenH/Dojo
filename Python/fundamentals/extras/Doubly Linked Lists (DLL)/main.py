from classes.dllist import DLList

dllist = DLList()
dllist.add_to_back(1).add_to_back(2).add_to_back(3).add_to_back(4).add_to_back(5).add_to_back(6).print_values()
print(f"List's length : {dllist.len}")
dllist.delete_node(3)
dllist.print_values()
print(f"List's length : {dllist.len}")
