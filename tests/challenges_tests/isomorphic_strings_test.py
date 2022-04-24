import unittest
from challenges.isomorphic_strings import is_isomorphic

class TestIsomorphicStrings(unittest.TestCase):

    def test_is_isomorphic(self):
        self.assertTrue(is_isomorphic("egg", "all"))
        self.assertFalse(is_isomorphic("wow", "aaa"))
        self.assertTrue(is_isomorphic("wow", "wiw"))
        self.assertFalse(is_isomorphic("wow", "win"))
        self.assertFalse(is_isomorphic("won", "winter"))