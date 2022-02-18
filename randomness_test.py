import unittest
from randomness import get_random_number

class TestRandomness(unittest.TestCase):

    def test_get_random_number(self):
        self.assertIn(get_random_number(), range(1,101))