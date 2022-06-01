'''
ANAGRAMS IN A STRING
Given a string original and a string check, find the starting index of all 
substrings of original that is an anagram of check. The output must be sorted 
in ascending order.

Output: 
A list of integers representing the starting indices of all anagrams of check.

Constraints:
- 1 <= len(original), len(check) <= 10^5
- Each string consists of only lowercase characters in standard English alphabet.
'''

from typing import List

def find_anagrams_in_string(text: str, check: str) -> List:
    
    left = 0
    right = len(check)
    indexes = []

    while right<=len(text):
        if ''.join(sorted(text[left:right])) == check:
            indexes.append(left)
        
        left += 1
        right += 1
    
    return indexes
