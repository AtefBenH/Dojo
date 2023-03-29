from classes.dlnode import DLNode

class DLList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_to_back(self, value) :
        #If the list is empty
        if self.head == None :
            new_node = DLNode(value)
            self.len+=1
            self.head = new_node
            self.tail = new_node
        #List not empty
        else :
            new_node = DLNode(value)
            self.len+=1
            pointer = self.tail
            pointer.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return self
    
    def print_values (self) :
        pointer = self.head
        if pointer != None :
            while (pointer != None) :
                print(pointer.value)
                pointer = pointer.next
        else :
            print ("Empty List")
        return self
