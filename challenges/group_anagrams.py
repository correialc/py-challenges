# Each list of anagrams has to be sorted
# The anagrams collection has to be sorted by the first term
# Hash table strategy with sorting
def group_anagrams(strs):
    
    anagrams = dict()

    # Identify anagrams
    for term in strs: 
        anagram_base_chars = "".join(sorted(term)) 
        if anagram_base_chars in anagrams:
            anagrams[anagram_base_chars].append(term)
        else:
            anagrams[anagram_base_chars] = [term]

    return list(anagrams.values())
            