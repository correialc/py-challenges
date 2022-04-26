'''
Given a sorted array of integers and an integer called target, 
find the element that equals to the target and return its index. 
If the element is not found, return -1.
'''
# Time complexity must be less then O(n)
# Strategy: binary search O(log(n))
def binary_search(arr, target):
    
    left = 0
    right = len(arr)-1

    while (left<=right):
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right=mid-1
        else:
            left=mid+1

    return -1 