def find_double_letters(word):
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            return True
    return False