# Search Insert Position

**Easy**

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Example 4:**

```
Input: nums = [1,3,5,6], target = 0
Output: 0
```

**Example 5:**

```
Input: nums = [1], target = 0
Output: 0
```

 

## **Solution**

```
#binary search
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, left, right, target):
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if len(nums[mid:right]) == 1:
                    return right
                index = binarySearch(nums, mid, right, target)
            else:
                if len(nums[left:mid]) == 1:
                    return mid
                index = binarySearch(nums, left,mid,target)
            return index
        left = 0
        right = len(nums) - 1
        
        if target <= nums[left]:
            return 0
        if target == nums[right]:
            return right
        if target > nums[right]:
            return right+1
        index = binarySearch(nums, left, right, target)
        return index
```



```
#array
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return i+1
```

