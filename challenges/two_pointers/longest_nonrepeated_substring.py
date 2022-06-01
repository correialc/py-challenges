def find_longest_substring(text: str) -> int:
    left = 0
    right = 0
    longest = 0
    sub = ""
    sub_size = 0

    while right<len(text):
        if text[right] in sub:
            while text[left] != text[right]:
                left+=1
            
            left += 1
            right += 1
            sub = text[left:right]
            sub_size = len(sub)
        else:
            sub += text[right]
            longest = max(longest, len(sub))
            right += 1 

    return longest

if __name__ == "__main__":
    find_longest_substring('abcdbea')