def binary_search(nums, start, end):

    mid = int(start+(end-start)/2)
    if nums[end] > nums[start]:
        return start
    if nums[end] < nums[start]:
        if nums[mid] < nums[start]:
            return binary_search(nums,start,mid)
        return binary_search(nums,mid+1,end)

    if len(nums) > 1 and mid != end and nums[mid] > nums[mid+1]:
        return mid+1
    return mid
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        mid = binary_search(nums, start, end)

        return nums[mid]