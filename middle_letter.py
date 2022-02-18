def find_middle_letter(one_string):
    if len(one_string)%2:
        return one_string[len(one_string)//2]
    
    return ""