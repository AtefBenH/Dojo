from classes.slnode import SLNode

class SLList :
    
    def __init__(self):
        self.head = None
        self.len = 0   #The lenght of the list
    
    #Add a node to the front
    def add_to_front(self, value) :
        new_node = SLNode(value) #creating the node
        self.len = self.len + 1 #incrementing the lenght 
        new_node.next = self.head #Our node.next will point at what node the head was pointing at
        self.head = new_node # And the head points now at our new node
        return self

    #Add a node to the back
    def add_to_back(self, value) :
        # if the list is empty, adding to the back is the same as adding to the front
        if self.head == None :
            self.add_to_front(value)
            return self
        # if the list is not empty
        new_node = SLNode(value) #creating the node
        self.len = self.len + 1 #incrementing the lenght 
        pointer = self.head
        while (pointer.next != None) :
            pointer = pointer.next
        # pointer is now at the back of the list 
        pointer.next = new_node 
        return self

    def remove_from_front(self) :
        #edge case : if the list is empty 
        if self.head == None :
            print("Nothing to remove, the list is empty")
            return self
        pointer = self.head
        self.head = self.head.next
        self.len = self.len - 1 #decrementing the lenght 
        return pointer.value
    
    def remove_from_back(self) :
        #edge case : if the list is empty 
        if self.head == None :
            print("Nothing to remove, the list is empty")
            return self
        pointer = self.head
        while (pointer.next != None) :
            before = pointer
            pointer = pointer.next
        before.next = None
        self.len = self.len - 1 #decrementing the lenght 
        return pointer.value
    
    # Remove the first node with the given value
    def remove_val(self, value) :
        pointer = self.head
        #if the node is the front 
        if (pointer.value == value) : 
            self.len = self.len - 1 #decrementing the lenght 
            return self.remove_from_front()
        #if the node is in the middle 
        while (pointer.next != None) :
            if (pointer.value == value) :
                before.next = pointer.next
                self.len = self.len - 1 #decrementing the lenght 
                return pointer.value
            before = pointer # We are saving the node before the next node, it's actually the current node
            pointer = pointer.next
        #if the node is in the back 
        if pointer.value == value :
            self.len = self.len - 1 #decrementing the lenght 
            return self.remove_from_back()
        # edge case : if the "Value" doesn't exist in the list
        print(f"Nothing to remove, there is no {value} in the list")
        return self
    
    def insert_at(self, value, position) : 
        # edge case : if the position is not an integer
        if type(position) != int :
            print("insert_at() needs an integer as a position")
            return self
        # edge case : if the position is negativ or greater than the lenght of the list
        if (position > self.len) or (position < 0) :
            print(f"position out of range, there is only {self.len} elements in the list")
            return self
        # inserting to the front
        if position == 0 :
            return self.add_to_front (value)
        # inserting to the back
        if position == self.len :
            return self.add_to_back(value)
        # inserting in the middle of the list
        pointer = self.head
        for i in range (1, self.len) : # notice that "pointer" is at the first node (index : 0) and i has the "index" of the second node
            if i==position :
                new_node = SLNode(value) #creating the node
                self.len = self.len + 1 #incrementing the lenght 
                new_node.next = pointer.next
                pointer.next = new_node
                return self
            pointer = pointer.next


    def print_values(self) :
        pointer = self.head
        while (pointer != None) :
            print (pointer.value)
            pointer = pointer.next
        return self