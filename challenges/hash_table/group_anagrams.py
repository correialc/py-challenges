def group_anagrams(strs):

    anagrams = dict()

    # Identify anagrams
    for term in strs:
        anagram_group_id = "".join(sorted(term))
        if anagram_group_id in anagrams:
            anagrams[anagram_group_id].append(term)
        else:
            anagrams[anagram_group_id] = [term]

    # Sorting results
    for anagram_group in anagrams.values():
        anagram_group.sort()

    anagrams = list(anagrams.values())
    anagrams.sort(key=lambda anagram_group: anagram_group[0])

    return anagrams
