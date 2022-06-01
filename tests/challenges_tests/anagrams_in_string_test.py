import unittest
from challenges.two_pointers.anagrams_in_string import find_anagrams_in_string

class TestAnagramsInString(unittest.TestCase):

    def test_find_anagrams_in_string(self):
        self.assertEqual(find_anagrams_in_string('cbaebabacd', 'abc'), [0, 6])
        self.assertEqual(find_anagrams_in_string('abab', 'ab'), [0, 1, 2])
        self.assertEqual(find_anagrams_in_string('nabanabannaabbaanana', 'banana'), [0, 3, 5, 6, 7, 13])
        self.assertEqual(find_anagrams_in_string('wubudubuwubuthattrue', 'ubutu'), [])
        self.assertEqual(find_anagrams_in_string('act', 'cact'), [])
        self.assertEqual(find_anagrams_in_string(
                            'thequickbrownfoxjumpsoverthelazydog', 
                            'thelazydogjumpsoverthequickbrownfox'), 
                            [0])