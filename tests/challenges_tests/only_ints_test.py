import unittest
from challenges.only_ints import is_only_ints

class TestOnlyInts(unittest.TestCase):

    def test_is_only_ints(self):
        self.assertTrue(is_only_ints(1, 2))
        self.assertFalse(is_only_ints(1, 'b'))
        self.assertFalse(is_only_ints('a', 2))
        self.assertFalse(is_only_ints('a', 'b'))