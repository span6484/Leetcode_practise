### 33. Search in Rotated Sorted Array

**Medium**			

### Question

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

 

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1
```

 

**Constraints:**

- `1 <= nums.length <= 5000`
- `-104 <= nums[i] <= 104`
- All values of `nums` are **unique**.
- `nums` is guaranteed to be rotated at some pivot.
- `-104 <= target <= 104`



### 思路 ：

- eliminate each cases includes: `len == 1   nums[left]    nums[right]`

* determine is_rotate via move **left and right points**：

  + Not rotate:	`nums[right] > nums[left]`

    1. straightly **BinarySearch**

  + Is_rotate：    

    1. Compare **target** and **nums[right]**, determine the main direction
    2. Find the special cases according to the  relationship between `target, mid, right`

    

* **重点是要清楚target 与 mid 与 end 三者关系** 
        

![image](https://user-images.githubusercontent.com/37071362/116379516-a89cf300-a845-11eb-887b-388b330c9b95.png)



### Solution

40ms 14.6M

```python
class Solution:    
    def search(self, nums, target):
        def binarySearch(nums, left, right, target):
            index = -1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if len(nums[left:right+1]) == 2:
                return index
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            
            is_Rotate = False
            if nums[left] > nums[right]:
                is_Rotate = True
						#core step here
            if is_Rotate:
                if target > nums[right]:
                    if target > nums[mid] and nums[mid] > nums[right]:
                        index = binarySearch(nums, mid, right, target)  
                    else:
                        index = binarySearch(nums, left, mid, target)
                else:
                        if target < nums[mid] and nums[mid] < nums[right]:
                            index = binarySearch(nums, left, mid, target)

                        else:
                            index = binarySearch(nums, mid, right, target)
            
            else:
                if target > nums[right]:
                    return -1
                if target < nums[left]:
                    return -1
                if target > nums[mid]:
                    index = binarySearch(nums, mid, right, target)
                else:
                    index = binarySearch(nums, left, mid, target)

            return index

        index = -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return index
        
        left = 0
        right = len(nums) -1
        index = binarySearch(nums, left, right, target)
        return index

#test case
# nums = [6,1,2,3,4,5]
# target = 1
# nums = [6,7,8,1,2,3,4,5]
# nums = [4,5,6,7,0,1,2]
nums = [7,1,2,3,4,5,6]
# nums = [1,3,5] 
# target = 2
for i in nums:
    print(f'--------check {i}-------')
    a = Solution().search(nums,i)
    print(f'the index is {a}')
    print(' ')

# a = Solution().search(nums,target)

# print(f'the index is {a}')
# print(' ')
```

