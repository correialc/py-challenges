import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList("Google")

    def test_constructor(self):
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.head.value, "Google")
        self.assertEqual(self.list.tail.value, "Google")
        self.assertIs(self.list.head, self.list.tail)

    def test_append(self):
        self.list.append("Udemy")
        self.assertEqual(self.list.length, 2)
        self.assertEqual(self.list.head.value, "Google")
        self.assertEqual(self.list.tail.value, "Udemy")

    def test_prepend(self):
        self.list.prepend("Discord")
        self.assertEqual(self.list.length, 2)
        self.assertEqual(self.list.head.value, "Discord")
        self.assertEqual(self.list.tail.value, "Google")

    def test_pop(self):
        self.list.append("Amazon")
        pop_node = self.list.pop()
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.head.value, "Google")
        self.assertEqual(self.list.tail.value, "Google")
        self.assertEqual(pop_node.value, "Amazon")

    def test_insert(self):
        self.list.append("Amazon")
        self.list.insert("Udemy", 1)
        self.assertEqual(self.list.length, 3)
        self.assertEqual(self.list.head.value, "Google")
        self.assertEqual(self.list.tail.value, "Amazon")

    def test_delete(self):
        self.list.append("Amazon")
        self.list.append("Udemy")
        self.list.delete(1)
        self.assertEqual(self.list.length, 2)
        self.assertEqual(self.list.head.value, "Google")
        self.assertEqual(self.list.tail.value, "Udemy")

    def test_pop_empty_list(self):
        self.list.pop()
        self.assertEqual(self.list.length, 0)
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)
    
    def test_append_empty_list(self):
        self.list.pop()
        self.list.append("Udemy")
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.head.value, "Udemy")
        self.assertEqual(self.list.tail.value, "Udemy")

    def test_insert_empty_list(self):
        
        self.list.pop()
        
        self.list.insert("Udemy", 99)
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.head.value, "Udemy")
        self.assertEqual(self.list.tail.value, "Udemy")
        
        self.list.pop()
        self.list.insert("Udemy", 0)
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.head.value, "Udemy")
        self.assertEqual(self.list.tail.value, "Udemy")

    def test_delete_empty_list(self):
        
        self.list.pop()

        self.list.delete(99)
        self.assertEqual(self.list.length, 0)
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)
        
        self.list.delete(0)
        self.assertEqual(self.list.length, 0)
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)

        