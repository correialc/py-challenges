import unittest
from challenges.binary_search.vanilla_binary import binary_search

class TestVanillaBinary(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 13, 27, 44, 81], 44), 3)
        self.assertEqual(binary_search([1, 13, 27, 44, 81], 13), 1)
        self.assertEqual(binary_search([1, 13, 27, 44, 81], 90), -1)
        self.assertEqual(binary_search([1, 13, 44, 81], 44), 2)
        self.assertEqual(binary_search([1, 13, 44, 81], 13), 1)
        self.assertEqual(binary_search([1, 13, 44, 81], 90), -1)
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)
        self.assertEqual(binary_search([], 1), -1)