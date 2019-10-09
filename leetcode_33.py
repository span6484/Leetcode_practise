def rank(key, a, lo, hi):
    if lo > hi:
        return -1
    mid = int(lo + (hi - lo) / 2)
    if key < a[mid]:
        return rank(key,a, lo, mid-1)
    elif key > a[mid]:
        return rank(key, a, mid + 1, hi)
    return mid
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        mid = 0
        is_order = True
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i+1]:
                mid = i
                is_order = False
        start = 0
        end = len(nums) - 1
        index = -1
        if is_order == True:
            index = rank(target, nums, start, end)
            
        if is_order == False and mid >= start and target >=nums[start] and target <=nums[mid]:
            index = rank(target, nums, start, mid)
            
        elif is_order == False and end > mid and target >= nums[mid+1] and target <= nums[end]:
            index = rank(target, nums, mid+1, end)
        
        return index
                