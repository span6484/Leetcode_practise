def binary_search(nums, start, end, target):
    mid = int(start + (end - start)/2)
    if nums[end] > nums[start]:
        if target < nums[mid]:
            # [1,3] t:0
            if mid == 0:
                return -1
            return binary_search(nums, start, mid-1, target)
        elif target > nums[mid]:
            return binary_search(nums, mid+1, end, target)
    if nums[end] < nums[start]:
        if target <= nums[end] and nums[mid] > target:
            return binary_search(nums, mid+1, end, target)
        if target > nums[end] and nums[mid] > target:
            return binary_search(nums, start, mid - 1, target)
    if nums[mid] != target:
        return -1
    return mid
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        start = 0
        end = len(nums) - 1
        index = binary_search(nums, start, end, target)
        return index