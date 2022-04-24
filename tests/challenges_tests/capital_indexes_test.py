import unittest
from challenges.capital_indexes import find_capital_indexes

class TestCapitalIndexes(unittest.TestCase):

        def test_find_capital_indexes(self):
                self.assertEqual(find_capital_indexes("HellO!"), [0, 4])