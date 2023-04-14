from dlnode import DLNode

class DLList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_to_back(self, value) :
        #If the list is empty
        if self.head == None : # Or, self.len == 0
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
            new_node.next = None
            self.tail = new_node
        return self
    
    def add_to_front(self, value) :
        #If the list is empty
        if  self.len == 0 : # Or, self.head == None
            self.add_to_back(value)
        #List not empty
        else :
            new_node = DLNode(value)
            self.len+=1
            pointer = self.head
            pointer.prev = new_node
            new_node.next = self.head
            self.head = new_node
        return self
    #insert a value at a certain position
    def insert_value_at (self, value, position) :
        if position == 0 : #if position is the head of the list
            self.add_to_front(value)
            return self
        elif position == self.len: #if position is the tail of the list
            self.add_to_back(value)
            return self
        else : #if position is in the middle of the list
            pointer = self.head
            for i in range (0, self.len) :
                if i == position :
                    new_node = DLNode(value)
                    self.len+=1
                    before.next = new_node
                    new_node.next = pointer
                    pointer.prev = new_node
                    new_node.prev = before
                    return self
                else :
                    before = pointer
                    pointer = pointer.next
            print(f"Position : {position} is out of range, the length of the list is : {self.len}")
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
        #If the value is in the middle of the list
        while (pointer!= None) :
            if (pointer.value == value):
                pointer = pointer.next
                before.next = pointer
                pointer.prev = before
                self.len-=1
                print("Node in the middle deleted")
                return self
            before = pointer
            pointer = pointer.next
        print(f"Nothing to remove, the element : {value} doesn't exist")
        return self
    def print_values (self) :
        pointer = self.head
        if self.len != 0 :
            if pointer != None :
                while (pointer != None) :
                    print(pointer.value)
                    pointer = pointer.next
        else :
            print ("Empty List")
        return self
