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
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length+=1

    def pop(self):
        pointer_node = self.lookup(self.length-1)
        pop_node = pointer_node.next
        pointer_node.next = None
        self.tail = pointer_node
        self.length-=1

        return pop_node

    def insert(self, value, index):
        new_node = Node(value)
        pointer_node = self.lookup(index)
        new_node.next = pointer_node.next
        pointer_node.next = new_node
        self.length+=1

    def delete(self, index):
        pointer_node = self.lookup(index)
        pointer_node.next = pointer_node.next.next
        self.length-=1

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
