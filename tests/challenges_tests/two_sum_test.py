import unittest
from challenges.two_sum import find_two_sum

class TestTwoSum(unittest.TestCase):

    def test_find_two_sum(self):
        self.assertEqual(find_two_sum([2,7,11,15], 9), [0,1])
        self.assertEqual(find_two_sum([3,2,4], 6), [1,2])
        self.assertEqual(find_two_sum([2,7,11,15], 8), [])
        self.assertEqual(find_two_sum([], 5), [])
        self.assertEqual(find_two_sum([4, 3, 4, 2, 1], 8), [0,2])
        self.assertEqual(find_two_sum([4,4], 8), [0,1])
        