def binary_search(nums, start, end, target):
    mid = int(start + (end - start)/2)
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    if mid == start or mid == end:
        if nums[mid] != target:
            return -1
    if nums[mid] == target:
        return mid
    if nums[end] > nums[start]:
        if target < nums[mid] and mid > 0:
            return binary_search(nums, start, mid-1, target)
        return binary_search(nums, mid+1, end, target)
    elif nums[end] < nums[start]:
        if target < nums[end]:
            if nums[mid] > nums[end]:
                return binary_search(nums, mid+1 , end, target)
            else:
                if nums[mid] < target:
                    return binary_search(nums, mid+1 , end, target)
                return binary_search(nums, start, mid-1, target)
        else:
            if nums[mid] > nums[end]:
                if nums[mid] < target:
                    return binary_search(nums,mid+1, end, target)
                return binary_search(nums, start, mid - 1, target)
            else:
                if nums[mid] < target:
                    return binary_search(nums,start, mid-1, target)
                return binary_search(nums,mid+1, end, target)
    else:
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

nums = [3,1,2]
targert = 1
answer = search()