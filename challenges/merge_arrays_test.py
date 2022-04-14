import unittest
from merge_arrays import merge_ordered_arrays

class TestMergeArrays(unittest.TestCase):
    
    def test_merge_ordered_arrays(self):
        self.assertEqual(merge_ordered_arrays([0, 3, 4, 31], [4, 6, 30]), [0, 3, 4, 4, 6, 30, 31])
        self.assertEqual(merge_ordered_arrays([], [4, 6, 30]), [4, 6, 30])
        self.assertEqual(merge_ordered_arrays([0, 3, 4, 31], []), [0, 3, 4, 31])
        self.assertEqual(merge_ordered_arrays([], []), [])
