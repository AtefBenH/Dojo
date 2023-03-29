from classes.sllist import SLList

#Creating a list
my_list = SLList() 

print("----------------------------------------------------------------")
print(f"The list is empty, the lenght of the list is : {my_list.len}")
print("----------------------------------------------------------------")
#Add some nodes to our list and print their values
print("---------------- This is the original S_L_list -----------------")
my_list.add_to_front("Name is").add_to_front("My").add_to_front("Hi!!!!").add_to_back("Bond").add_to_back(
    "James Bond").print_values() #Chaining is cool, right ?!!
print("-------------------------------------------")
print(f"the lenght of the list is : {my_list.len}")
print("-------------------------------------------")
# Remove from the front of the node
x = my_list.remove_from_front()
print(f"------ We now removed the front of the list, this is its values : {x} ------")
print("---------- This is the he new S_L_list after removing the front node --------")
my_list.print_values()
print("-------------------------------------------")
print(f"the lenght of the list is : {my_list.len}")
print("-------------------------------------------")
# Remove from the back of the node
x = my_list.remove_from_back()
print(f"------- We now removed the back of the list, this is its values : {x} -------")
print("----------- This is the he new S_L_list after removing the back node ---------")
my_list.print_values()
print("-------------------------------------------")
print(f"the lenght of the list is : {my_list.len}")
print("-------------------------------------------")
# Remove the first node with the given value
value = "Name is"
print(f"----------- This is the he new S_L_list after removing  : {value} -----------")
my_list.remove_val(value)
my_list.print_values()
print("-------------------------------------------")
print(f"the lenght of the list is : {my_list.len}")
print("-------------------------------------------")
#Insert a value at the nth position
my_list.insert_at("007", 1)
my_list.print_values()
print("-------------------------------------------")
print(f"the lenght of the list is : {my_list.len}")
print("-------------------------------------------")

