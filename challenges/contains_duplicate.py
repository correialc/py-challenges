# Unordered array
# Hash table strategy
def contains_duplicate(nums):
    
    found_numbers = dict()
    
    for n in nums: # O(n)
        if n in found_numbers: # O(1)
            return True
        else:
            found_numbers[n] = True # O(1)
    
    return False