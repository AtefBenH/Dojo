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

    def delete_node(self, value):
        #If the value is the last one in the list
        pointer = self.tail
        if pointer.value == value :
            pointer = pointer.prev
            self.tail = pointer
            pointer.next = None
            self.len-=1
            print("Back node deleted")
            return self
        #If the value is the first of the list
        pointer = self.head
        if pointer.value == value :
            pointer = pointer.next
            self.head = pointer
            pointer.prev = None
            self.len-=1
            print("Front node deleted")
            return self
        
        while (pointer!= None) :
            if (pointer.value == value):
                pointer = pointer.next
                last.next = pointer
                pointer.prev = last
                self.len-=1
                print("Node in the middle deleted")
                return self
            last = pointer
            pointer = pointer.next
        print(f"Nothing to remove, the element : {value} doesn't exist")
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
