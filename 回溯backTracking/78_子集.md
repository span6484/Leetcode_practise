#### [78. 子集](https://leetcode.cn/problems/subsets/)

难度中等1749收藏分享切换为英文接收动态反馈

给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**示例 2：**

```
输入：nums = [0]
输出：[[],[0]]
```

 

**提示：**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- `nums` 中的所有元素 **互不相同**





## Solution

1. **是无序，取过的元素不会重复取，写回溯算法的时候，for就要从startIndex开始，而不是从0开始！**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        path = list()
        
        def backTracking(startIndex):
            result.append(path[:])			#先添加
            if (startIndex >= len(nums)):		
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backTracking(i+1)
                path.pop()
        backTracking(0)
        return result
```

![78.子集](https://img-blog.csdnimg.cn/202011232041348.png)