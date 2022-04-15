# Unsorted array
# Can have duplicated items
def find_two_sum(nums, target):
    p1 = 0
    p2 = len(nums) - 1

    num_position = {nums[i]: i for i in range(0, len(nums))} # O(n)
    nums.sort() # O(n log n)

    while p1 < p2: # O(n)
        
        numsum = nums[p1] + nums[p2]

        if numsum == target:
            return [num_position[nums[p1]], num_position[nums[p2]]] # O(1)
        elif numsum < target:
            p1+=1
        else:
            p2-=1
    
    return []