#### [46. 全排列](https://leetcode.cn/problems/permutations/)

难度中等2168

给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**

```
输入：nums = [1]
输出：[[1]]
```





## Solution

[代码回忆录_全排列](https://www.programmercarl.com/0046.全排列.html#思路)

1. 这道题是不含重复数字的序列

1. **排列是有序的**, **也就是说 [1,2] 和 [2,1] 是两个集合**， 
2. 排列问题需要一个**used**数组，标记已经选择的元素
3. **used数组，其实就是记录此时path里都有哪些元素使用了，一个排列里一个元素只能使用一次**。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backTracking(visited_lst):
            if (len(path) == len(nums)):
                result.append(path[:])
                return 
            for i in range(0, len(nums)):
                if visited_lst[i] == True:
                    continue
                path.append(nums[i])
                visited_lst[i] = True
                backTracking(visited_lst)
                path.pop()
                visited_lst[i] = False
        visited_lst = [False] * len(nums)
        backTracking(visited_lst)
        return result
```

