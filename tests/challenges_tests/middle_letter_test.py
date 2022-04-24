import unittest
from challenges.middle_letter import find_middle_letter

class TestMiddleLetter(unittest.TestCase):

    def test_find_middle_letter(self):
        self.assertEqual(find_middle_letter("abc"), "b")
        self.assertEqual(find_middle_letter("abcde"), "c")
        self.assertEqual(find_middle_letter("abcdef"), "")
        