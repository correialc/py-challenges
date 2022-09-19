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
    contained = dict()

    left, right = 0, 0
    subs = ""
    minsubs = ""
    
    while right < len(original):
        
        while len(contained) < len(count_check) and right < len(original):
            if original[right] in count_check:
                count_subs.update(original[right])
                
                if count_subs[original[right]] >= count_check[original[right]]:
                    contained[original[right]] = True
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

        count_subs[original[left]] -= 1
        if original[left] in contained:
            del contained[original[left]]
        left+=1

    return minsubs

if __name__ == '__main__':
    original = "aabbababaabaabbaaabbabbabbaabbabaabbabbbbabbaaababbaabb"
    check = "bababa"
    res = get_minimum_window(original, check)
    print(res)