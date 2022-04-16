import unittest
from contains_duplicate import contains_duplicate

class TestContainsDuplicate(unittest.TestCase):

    def test_contains_duplicate(self):
        self.assertTrue(contains_duplicate([1,2,3,1]))
        self.assertFalse(contains_duplicate([1,2,3,4]))
        self.assertTrue(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
        self.assertFalse(contains_duplicate([1]))
        self.assertFalse(contains_duplicate([]))