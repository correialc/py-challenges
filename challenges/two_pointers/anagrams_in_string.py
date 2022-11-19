from collections import Counter
from typing import List


def find_anagrams_in_string(text: str, check: str) -> List:

    left = 0
    right = len(check)
    check = Counter(check)
    window = Counter(text[left:right])
    indexes = []

    while right <= len(text):
        if window == check:
            indexes.append(left)

        left += 1
        right += 1
        window = Counter(text[left:right])
    return indexes
