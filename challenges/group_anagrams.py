# Any order for each anagram
# Any order for the list of anagrams
# Hash table strategy with sorting
def group_anagrams(strs):
    
    found_str = dict()

    for s in strs: 
        base_str = "".join(sorted(s)) 
        if base_str in found_str:
            found_str[base_str].append(s)
        else:
            found_str[base_str] = [s]

    return list(found_str.values())
            