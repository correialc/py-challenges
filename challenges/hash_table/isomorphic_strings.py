def is_isomorphic(str1, str2):

    chars = dict()
    found_chars = set()

    if len(str1) != len(str2):
        return False

    for i in range(0, len(str1)):
        if str1[i] in chars:
            if chars[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in found_chars:
                return False
            else:
                chars[str1[i]] = str2[i]
                found_chars.add(str2[i])

    return True
