def maxSubArray(nums):
    index = 0
    if len(nums) == 1:
        return nums[index]
    if max(nums) <= 0:
        return max(nums)
    while nums[0] < 0:
        index += 1
        nums = nums[index:]
        index = 0
    current = nums[0]
    add = 0
    glob = nums[0]
    for i in nums:
        current = i
        if add<0:
            add = current
        else:
            add += current
        compare_CA = max(current, add)
        if glob < compare_CA:
            if compare_CA == add:
                glob = add
            else:
                add = current
                glob = current
        print('')
        print('current: ', current)
        print('add    : ', add)
        print('glob:    ', glob)
    return glob
nums = [2,0,-3,2,1,0,1,-2]
max_value = maxSubArray(nums)
print(max_value)
