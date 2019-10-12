def binary_search(nums, start, end):
    mid = int(start+(end-start)/2)
    # [1,2,3,4,5]   ->
    if nums[end] > nums[start]:
        return start
    if nums[end] < nums[start]:
        # [3,1,2]  <-—·
        if nums[mid] < nums[start]:
            return binary_search(nums,start,mid)
        #[5,1,2,3]   ->
        return binary_search(nums,mid+1,end)
    return mid
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        mid = binary_search(nums, start, end)

        return nums[mid]