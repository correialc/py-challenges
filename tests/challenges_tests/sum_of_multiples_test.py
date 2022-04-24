import unittest
from challenges.sum_of_multiples import calc_sum_multiples 

class TestSumMultiples(unittest.TestCase):

    def test_calc_sum_multiples(self):
        self.assertEqual(calc_sum_multiples(10, 3, 5), 23)