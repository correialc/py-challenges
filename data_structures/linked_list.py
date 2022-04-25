class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length = 1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1

    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length = 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.length+=1

    def pop(self):
        
        if self.length == 0:
            return None
        
        if self.length == 1:
            pop_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return pop_node

        pointer_node = self.lookup(self.length-1)
        pop_node = pointer_node.next
        pointer_node.next = None
        self.tail = pointer_node
        self.length-=1

        return pop_node

    def insert(self, value, index):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length = 1
            return
        
        pointer_node = self.lookup(index)
        new_node.next = pointer_node.next
        pointer_node.next = new_node
        self.length+=1

    def delete(self, index):
        
        if self.length == 0:
            return
        
        pointer_node = self.lookup(index)
        pointer_node.next = pointer_node.next.next
        self.length-=1

    def reverse(self):
        lead_node_index = self.length-1
        swap_node = self.lookup(lead_node_index)
        lag_node = self.lookup(lead_node_index-1)

        swapped_nodes = 0

        while swapped_nodes < self.length - 1:
            
            self.tail.next = swap_node
            self.tail = swap_node
            
            if swap_node != self.head:
                lag_node.next = swap_node.next
            else:
                self.head = swap_node.next

            swap_node.next = None

            swapped_nodes += 1
            lead_node_index = self.length - 1 - swapped_nodes
            swap_node = self.lookup(lead_node_index)
            lag_node = self.lookup(lead_node_index-1)

    def lookup(self, index):
        if index > self.length - 1:
            index = self.length - 1
        
        count=0
        pointer_node = self.head

        while count<(index-1):
            pointer_node = pointer_node.next
            count+=1

        return pointer_node

    def __str__(self):
        
        printed_list = "\nSIZE: "+str(self.length)
        printed_list += "\nHEAD: "+str(self.head.value)
        printed_list += "\nTAIL: "+str(self.tail.value)
        printed_list += "\n"

        node = self.head
        while node != None:
            printed_list += str(node.value) + " >> "
            node = node.next
        
        return printed_list
