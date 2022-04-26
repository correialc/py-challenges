# Find an item on a sorted array
# Time complexity restriction: less then O(n)
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