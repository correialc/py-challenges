import unittest
from challenges.first_recurrent_items import find_first_recurrent_items

class TestFirstRecurrentItems(unittest.TestCase):
    
    def test_find_first_recurrent_items(self):
        self.assertEqual(find_first_recurrent_items([1, 2 , 3, 1]), 1)
        self.assertEqual(find_first_recurrent_items([1, 2 , 1, 3]), 1)
        self.assertEqual(find_first_recurrent_items([2 , 1, 1, 3]), 1)
        self.assertEqual(find_first_recurrent_items([]), None)
        self.assertEqual(find_first_recurrent_items([1]), None)
        self.assertEqual(find_first_recurrent_items([1, 2, 3, 4]), None)
        self.assertEqual(find_first_recurrent_items(['a', 2, 'a', 4]), 'a')
        self.assertEqual(find_first_recurrent_items([1, 'b', 1, 4]), 1)