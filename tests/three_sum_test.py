import unittest
from challenges.two_pointers.three_sum import triplets_with_sum_zero

class TestThreeSum(unittest.TestCase):
    
    def test_triplets_with_sum_zero(self):
        self.assertEqual(triplets_with_sum_zero([-1, 0, 1, 2, -1, -4]), 
                                                [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(triplets_with_sum_zero([1, -1, 2, -2, 3, -3, 4, -4]), 
                                                [[-4, 1, 3], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]])