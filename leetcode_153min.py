def binary_search(nums, start, end):
    mid = int(start+(end-start)/2)
    if nums[end] < nums[start] and nums[mid] < nums[start]:
        return binary_search(nums,start,mid-1)
    if nums[end] < nums[start] and nums[mid] > nums[start] and nums[mid] < nums[end]:
        return binary_search(nums,mid+1,end)
    if nums[end] > nums[start] and nums[mid] > start:
        return binary_search(nums,start,mid-1)
    return mid
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums
        start = 0
        end = len(nums) - 1
        mid = binary_search(nums, start, end)

        return nums[mid]