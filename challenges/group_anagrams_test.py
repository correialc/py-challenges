import unittest
from group_anagrams import group_anagrams

class TestGroupAnagrams(unittest.TestCase):

    def test_group_anagrams(self):
        
        self.assertIn(["bat"], group_anagrams(["eat","tea","tan","ate","nat","bat"]))
        self.assertIn(["tan", "nat"], group_anagrams(["eat","tea","tan","ate","nat","bat"]))
        self.assertIn(["eat","tea", "ate"], group_anagrams(["eat","tea","tan","ate","nat","bat"]))
                
        self.assertEqual(group_anagrams([""]), [[""]])
        self.assertEqual(group_anagrams(["a"]), [["a"]])