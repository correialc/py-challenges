import unittest
from challenges.binary_search.finding_boundary import find_boundary

class TestVanillaBinary(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(find_boundary([False, False, False, True, True]), 3)
        self.assertEqual(find_boundary([False, True, True, True, True]), 1)
        self.assertEqual(find_boundary([False, False, False, False, False]), -1)
        self.assertEqual(find_boundary([False, False, True, True]), 2)
        self.assertEqual(find_boundary([False, True, True, True]), 1)
        self.assertEqual(find_boundary([False]), -1)
        self.assertEqual(find_boundary([True]), 0)
        self.assertEqual(find_boundary([]), -1)