'''
MINIMUM WINDOW SUBSTRING

Given two strings, original and check, return the minimum substring of original such that 
each character in check, including duplicates, are included in this substring. By "minimum", 
I mean the shortest substring. If two substrings that satisfy the condition has the same length, 
the one that comes lexicographically first are smaller.

Parameters
- original: The original string.
- check: The string to check if a window contains it.

Result
- The smallest substring of original that satisfy the condition.

'''

from collections import Counter

def get_minimum_window(original: str, check: str) -> str:
    count_check = Counter(check)
    count_subs = Counter()
    
    left, right = 0, 0
    subs = ""
    minsubs = ""
    
    while right < len(original):
        
        while len(count_check) != len(count_subs) and right < len(original):
            if original[right] in count_check:
                count_subs.update(original[right])
            right+=1
                
        while original[left] not in count_check or count_subs[original[left]] > count_check[original[left]]:
            if count_subs[original[left]] > count_check[original[left]]:
                count_subs[original[left]] -= 1
            left +=1
        
        if count_check == count_subs:
            subs = original[left:right]
        
        if len(subs)<len(minsubs) or len(minsubs) == 0:
            minsubs = subs
        elif len(subs) == len(minsubs):
            minsubs = min(subs, minsubs)

        del count_subs[original[left]]
        left+=1

    return minsubs

if __name__ == '__main__':
    original = "aabbababaabaabbaaabbabbabbaabbabaabbabbbbabbaaababbaabb"
    check = "bababa"
    res = get_minimum_window(original, check)
    print(res)