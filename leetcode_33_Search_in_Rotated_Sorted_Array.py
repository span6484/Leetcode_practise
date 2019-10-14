def binary_search(nums, start, end, target):
    mid = int(start + (end - start)/2)
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    if mid == start or mid == end:
        if nums[mid] != target:
            return -1
    if nums[end] > nums[start]:
        if target < nums[mid] and mid > 0:
            return binary_search(nums, start, mid-1, target)
        elif target > nums[mid] and mid < len(nums) - 1:
            return binary_search(nums, mid+1, end, target)
    if nums[end] < nums[start]:
        if target < nums[end] and target > nums[mid]:
            return binary_search(nums, mid+1 , end, target)
        if target < nums[end] and target < nums[mid]:
            return binary_search(nums, start, mid-1, target)
        if target > nums[end] and target < nums[mid]:
            return binary_search(nums, start, mid - 1, target)
        if target > nums[end] and target > nums[mid]:
            return binary_search(nums, mid+1, end, target)
    return mid
def search(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    start = 0
    end = len(nums) - 1
    index = binary_search(nums, start, end, target)
    if nums[index] != target:
        return -1
    return index

# erro test
nums = [4,5,6,7,0,1]    #not success
target = 0
for num in nums:
    val = search(nums, num)
    print(str(num) +' index is '+ str(val))