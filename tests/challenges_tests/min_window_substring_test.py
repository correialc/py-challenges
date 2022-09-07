import unittest
from challenges.two_pointers.min_window_substring import get_minimum_window

class TestMinWindowSubstring(unittest.TestCase):

    def test_get_minimum_window(self):
        self.assertEqual(get_minimum_window("cdbaebaecd", "abc"), "baec")
        self.assertEqual(get_minimum_window("aabbababaabaabbaaabbabbabbaabbabaabbabbbbabbaaababbaabb", "bababa"), "aababb")

    