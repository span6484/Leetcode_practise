# Permutations II

**Medium**

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

 

**Example 1:**

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

 

**Constraints:**

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## 解题思路：

1. 参照回溯模版和leetcode46

2. 通过used来判断走没走过 `used = [False] * len(nums) `

3.  注意设置3个条件

   ```
   i == 0 or nums[i] != nums[i-1] or used[i-1]
   ```

   如果访问过且大小相同，我们就不访问第二遍

4. We shouldn't store them at first time, and then check whether exists some dumplicate array, that will arise the complexity to **1256 ms**

## Solution

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        
        def backtrack(nums, temp, arr):
            if len(temp) == len(nums):
                print(used)
                arr.append(temp.copy())
                return arr
            
            for i in range(len(nums)):
                print('i', i)
                print(used)
                if not used[i]:
                    print(used[i-1])
                    if i == 0 or nums[i] != nums[i-1] or used[i-1] :
                        used[i] = True   
                        temp.append(nums[i])
                        arr = backtrack(nums,temp, arr)
                        temp.pop()
                        used[i] = False
            return arr
          
        temp = []
        arr = []
        nums = sorted(nums)
        arr = searchUnique(nums,temp, arr)
        
        return arr
        
```