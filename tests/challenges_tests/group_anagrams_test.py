import unittest
from challenges.hash_table.group_anagrams import group_anagrams

class TestGroupAnagrams(unittest.TestCase):

    def test_group_anagrams(self):
        
        self.assertEqual(group_anagrams(["eat","tea","tan","ate","nat","bat"]),
                                        [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])
                
        self.assertEqual(group_anagrams([""]), [[""]])
        self.assertEqual(group_anagrams(["a"]), [["a"]])