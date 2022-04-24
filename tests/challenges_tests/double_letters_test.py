import unittest
from challenges.double_letters import find_double_letters

class TestDoubleLetters(unittest.TestCase):

    def test_find_double_letters(self):
        self.assertFalse(find_double_letters('Rice'))
        self.assertTrue(find_double_letters('Better'))
