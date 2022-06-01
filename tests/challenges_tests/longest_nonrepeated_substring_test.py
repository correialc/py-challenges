import unittest
from challenges.two_pointers.longest_nonrepeated_substring import find_longest_substring

class TestLongestNonRepeatedSubstring(unittest.TestCase):

    def test_find_longest_substring(self):
        self.assertEqual(find_longest_substring('abcdbea'), 5)
        self.assertEqual(find_longest_substring('aba'), 2)
        self.assertEqual(find_longest_substring('abccabcabcc'), 3)
        self.assertEqual(find_longest_substring('aaaabaaa'), 2)
        self.assertEqual(find_longest_substring('a'), 1)
        self.assertEqual(find_longest_substring(''), 0)


