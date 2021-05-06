# Leetcode 912

## Topic: 	divide and conquer, Array Sort

<img src="https://user-images.githubusercontent.com/37071362/114265397-2a59e780-9a23-11eb-87e9-c6e8e06b90ba.png" alt="image-20210410171650786" style="zoom:40%;" />


## 思路历程：

### Bubble Sort   

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums_len  = len(nums)
        
        for i in range(nums_len):
            for j in range(nums_len-1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return nums
```

#### Result

```apl
	Time Limit Exceeded
```



### Insert Sort

```python
def insertSort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            (nums[j-1], nums[j]) = (nums[j], nums[j-1])
            j -= 1
    return nums
arr = [5,4,3,2,1]
new_arr = insertSort(arr)
print(arr)
```

Result:

```apl
	Time Limit Exceeded
```



### Quick Sort

O(nlogn)    

最坏情况  O(n*2)

```python
 return arr
   #quick sort
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr
def quickSortHelper(arr, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while leftIdx <= rightIdx:
        if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
            (arr[leftIdx], arr[rightIdx]) = (arr[rightIdx], arr[leftIdx])

        if arr[leftIdx] <= arr[pivotIdx]:
            leftIdx += 1
        if arr[rightIdx] >= arr[pivotIdx]:
            rightIdx -= 1
    (arr[pivotIdx], arr[rightIdx]) = (arr[rightIdx], arr[pivotIdx])

    #now we get sort 1 time arr, and we start the loop
    leftSubArrayLen = rightIdx - startIdx
    rightSubArrayLen = endIdx - rightIdx
    if leftSubArrayLen < rightSubArrayLen:
        quickSortHelper(arr, startIdx, rightIdx - 1)
        quickSortHelper(arr, rightIdx + 1, endIdx)
    else:
        quickSortHelper(arr, rightIdx + 1,  endIdx)
        quickSortHelper(arr, startIdx, rightIdx - 1)

arr = [49,38,65,97,76,13,27,49]

arr_new = quickSort(arr)
print(arr_new)
```

#### Result：

```apl
	Time Limit Exceeded
```



### Merge sort

- Memorization
- Divide to each and conquer
- 几乎等同递归但最后要combine每个小问题
- Backtraching

这一题将运用分治算法





#### 理解递归

递归思路必看： (https://www.zhihu.com/question/31412436/answer/683820765)



#### 模版

```python
def divide_and_conquer(s):
  #1) divide the problem into a set of subproblems
  [S1,S2, ... Sn] = divide(S)
  
  #2) solve the subproblem recursively,
 			# obtain the results of subproblems as [R1, R2... Rn].
  rets = [divide_and_conquer(Si) for Si in [S1,S2,...Sn]]
  [R1,R2,...Rn] = rets
  
  #3) combine the results from the subproblems.
  # and return the combined result.
  return combine([R1,R2,...RN])
```



#### 解题思路

[归并排序](https://www.youtube.com/watch?v=KAgkvtKMbwY)

<img src="/Users/shaoqiupan/Library/Application Support/typora-user-images/image-20210408113446465.png" alt="image-20210408113446465" style="zoom: 200%;" />





class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

```python
    def merge(nums, start, mid, end):
        left = nums[start:mid].copy()
        right = nums[mid:end].copy()
        new_array = []
        time_left = len(left)
        time_right = len(right)
        index_left = 0
        index_right = 0
        while index_left < time_left and index_right < time_right:
            if left[index_left] < right[index_right]:
                new_array.append(left[index_left])
                index_left += 1
            else:
                new_array.append(right[index_right])
                index_right += 1
        while index_left < time_left:
            new_array.append(left[index_left])
            index_left += 1
        while index_right < time_right:
            new_array.append(right[index_right])
            index_right += 1
        nums[start:end] = new_array
        return nums
    
    def divide(nums, left, right):
        mid = (left+right)//2

        if len(nums[left:mid]) > 1:
            nums = divide(nums, left, mid)
        if len(nums[mid:right]) > 1:
            nums = divide(nums, mid, right)
            
        nums = merge(nums, left, mid, right)
        return nums
    left = 0
    right = len(nums)
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums
    else:
        nums = divide(nums, left, right)
    
    return nums
```

- 学会画图来一步步跟踪， 每个递归都会开辟空间，理清思路(顺着管道走，有管道的地方优先走管道)

<img src="https://user-images.githubusercontent.com/37071362/114265464-7ad14500-9a23-11eb-8055-51dbe87de76a.png" alt="image-20210410171650786" style="zoom:40%;" />

------





## 本题难点

- 分而治之
- 递归的思路比较绕，要画图理解
- end的判定条件，要清楚每一步切片后的array是多少，有没有重复，通过print时刻跟踪
- 判断什么时候divide， 什么时候跳过divide， divide的判定条件很重要，当只有一个数时，跳过divide，留着merge
- 当end处于最后一个，一定要记得end+1， 因为 nums[1,2,3] 对于 nums[2:3]是取不到3的，得nums[2:4]

- 这一题除了merge sort， 其他三个都解不出来

## Summary for array sort



| sort        | 时间复杂度（average） | 时间复杂度（最好） | 时间复杂度 （最坏） | 空间复杂度 |
| ----------- | --------------------- | ------------------ | ------------------- | ---------- |
| Bubble sort | O(n**2)               | O(n)               | O(n**2)             | O(1)       |
| insert sort | O(n**2)               | O(n)               | O(n**2)             | O(1)       |
| quick sort  | O(nlogn)              | O(nlogn)           | O(n**2)             | O(nlogn)   |
| Merge sort  | O(nlogn)              | O(nlogn)           | O(nlogn)            | O(n)       |



