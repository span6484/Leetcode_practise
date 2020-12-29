from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left + 1 < right:
            
            mid = (left + right) // 2
            
            if (nums[mid] == target):
                return mid
            
            elif(nums[mid] < target):
                left = mid
            
            else:
                right = mid
                
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1
        

# test case
if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    res = Solution().search(nums, target)
    print(res)