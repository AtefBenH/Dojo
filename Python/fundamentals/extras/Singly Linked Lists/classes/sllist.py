from classes.slnode import SLNode
class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode (val)         #Create a new Node
        # current_head = self.head        #Saving the current head
        new_node.next = self.head    #Set the new node's next to the list's current head
        self.head = new_node            #Set the list's head to the node we created in the last step
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next    #Set the runner to its neighbor
        return self	                #Once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:	    #If the list is empty
            self.add_to_front(val)  #Run the add_to_front method
            return self	            #Let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node      #Increment the runner to the next node in the list
        return self                 #Return self to allow for chaining



