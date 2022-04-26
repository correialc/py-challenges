'''
Given a list of integers, return a list containing all unique triplets 
in the list such that the sum of the triplet is zero. Each triplet must 
be sorted in ascending order, and the resulting list must be sorted 
lexicographically.
'''
def triplets_with_sum_zero(nums):

    left = 0
    right = len(nums) - 1
    triplets = []

    nums.sort()

    while left<right:
        middle_item = binary_search_item(nums[left+1:right], (nums[left]+nums[right])*-1)
        if middle_item:
            triplets.append([nums[left], middle_item, nums[right]])
        elif nums[left]+nums[right]>0:
            right-=1
        else:
            left+=1
        

def binary_search_item(arr, target):

    left = 0
    right = len(arr) - 1

    while left<=right:
        mid = (left+right)//2

        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1

    return None

if __name__ == "__main__":
    triplets_with_sum_zero([-1, 0, 1, 2, -1, -4])

# [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2]
