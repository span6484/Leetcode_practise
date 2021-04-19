# 53. Maximum Subarray

Easy

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

 

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
```

 

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `-105 <= nums[i] <= 105`



该题不能用嵌套循环，会超出复杂度

### 方法一：指针比大小

1. 设置三个指针， current，add 和global,

2. 如果全是负数，那么直接选出nums中的最大， 否则我们就从第一个非负数开始计算
3. add是相加值的存储，当add值为负数，则用替换成current值
4. global值存入current 或add的最大值，或者不变，根据具体情况而定

<img src="https://user-images.githubusercontent.com/37071362/115192880-fdda5580-a11d-11eb-9cc9-5b3591cd7f7e.png" alt="image" style="zoom: 50%;" />



Solution1:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        index = 0
        if len(nums) == 1:
            return nums[index]
        #determine the all value are negative
        if max(nums) <= 0:
            return max(nums)
          
        #let nums[0] >= 0
        while nums[0] < 0:
            index += 1
            nums = nums[index:]
            index = 0
            
        current = nums[0]
        add = 0
        glob = nums[0]
        for i in nums:
            current = i
            if add < 0 :
                add = current
            else:
                add += current
            compare_CA = max(current, add)
            if glob < compare_CA:
                if compare_CA == add:
                    glob = add
                else:
                    add = current
                    glob = current
        return glob
```

