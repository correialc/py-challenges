# Traverse both strings in one single loop
# The order of the chars in the string can not be changed
# Hash table strategy
def is_isomorphic(str1, str2):
    
    chars = dict()

    if len(str1) != len(str2):
        return False

    for i in range(0, len(str1)):
        if str1[i] in chars:
            if chars[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in chars.values():
                return False
            else:
                chars[str1[i]] = str2[i]     

    return True
