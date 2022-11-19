def find_boundary(arr):

    left = 0
    right = len(arr)-1
    bound_index = -1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]:
            bound_index = mid
            right=mid-1
        else:
            left=mid+1
    
    return bound_index
