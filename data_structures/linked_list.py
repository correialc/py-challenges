class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        
        printed_list = "\nHEAD: "+str(self.head.value)
        printed_list += "\nTAIL: "+str(self.tail.value)
        printed_list += "\n"

        node = self.head
        while node != None:
            printed_list += str(node.value) + " >> "
            node = node.next
        
        return printed_list

l = LinkedList("Google")
l.append("Udemy")
print(l)
l.prepend("Discord")
print(l)