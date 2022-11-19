def find_two_sum(nums, target):
    p1 = 0
    p2 = len(nums) - 1

    positions = dict()

    for i in range(0, len(nums)):
        if nums[i] in positions:
            positions[nums[i]].append(i)
        else:
            positions[nums[i]] = [i]

    nums.sort()

    while p1 < p2:

        numsum = nums[p1] + nums[p2]

        if numsum == target:
            if nums[p1] == nums[p2]:
                return [positions[nums[p1]][0], positions[nums[p2]][1]]
            else:
                return [positions[nums[p1]][0], positions[nums[p2]][0]]
        elif numsum < target:
            p1 += 1
        else:
            p2 -= 1

    return []
