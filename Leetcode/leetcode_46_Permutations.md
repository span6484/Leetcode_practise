# 46. Permutations
**Medium**

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```

 

**Constraints:**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## 解题思路：

1. 创建两个list， 一个是result，一个是临时存储

2. 方法，使用递归， 通过递归来进一步获取数值，注意递归后每个会进行pop， 一次来达到清空目标数值要求，比如， 123 中要通过pop，来清除掉添加的2，3， 只剩1， 从而可以继续132


4. 关键词： 全排列， 回溯，递归， permutation
5. 笔记参考 Notability Python Permutations

![image-20210501084221755](/Users/shaoqiupan/Library/Application Support/typora-user-images/image-20210501084221755.png)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def search_target(nums, temp, arr):
            if len(temp) == len(nums):
                arr.append(temp.copy())
                return arr

            for i in nums:
                if i not in temp:
                    temp.append(i)
                    arr = search_target(nums, temp, arr)
                    temp.pop()
            return arr
        arr = []
        temp = []        
        arr = search_target(nums, temp,arr)
        return arr
```



```python
#rick Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len == 0:
            return nums
        
        if len == 1:
            return [nums]
        
        partical = []
        result = []
        self.getValue(partical, nums, len(nums), result)
        
        return result
    
    
    def getValue(self, partical, nums, lenNums, result):
        
        if lenNums == 0:
            result.append(list(partical))
            
        
        for i in nums:
            if i not in partical:
                partical.append(i)
                self.getValue(partical, nums, lenNums-1, result)
                partical.pop()
                
```

