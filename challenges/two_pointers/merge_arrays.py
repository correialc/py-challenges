def merge_ordered_arrays(arr1, arr2):
    max_lenght = len(arr1) + len(arr2)
    merged_array = []
    p1 = 0
    p2 = 0

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    # O(n + m)
    for i in range(0, max_lenght):
        if (p2 > len(arr2) - 1) or (arr1[p1] <= arr2[p2]):
            merged_array.append(arr1[p1])
            if p1 < len(arr1) - 1:
                p1 += 1
        else:
            merged_array.append(arr2[p2])
            if p2 <= len(arr2) - 1:
                p2 += 1
            else:
                p2 = None

    return merged_array
