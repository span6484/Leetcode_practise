# Leetcode 912

## Topic: 	divide and conquer, 分而治之

<img src="https://user-images.githubusercontent.com/37071362/114265397-2a59e780-9a23-11eb-87e9-c6e8e06b90ba.png" alt="image-20210410171650786" style="zoom:40%;" />


### 思路历程：

1. #### 冒泡排序

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

   #### 结果：

   ```apl
   	Time Limit Exceeded
   ```

   #### 原因：

   冒泡排序无法处理庞大的数组， 需要花费巨额的时间，这是效率最低的算法  



2. ### Recursion

   - Memorization

   - ### Divide and conquer

     - 几乎等同递归但最后要combine每个小问题

   - Backtraching

   这一题将运用分治算法





### 理解递归

##### ***递归思路必看： (https://www.zhihu.com/question/31412436/answer/683820765)



### 模版：

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



### 解题思路：

[归并排序](https://www.youtube.com/watch?v=KAgkvtKMbwY)

<img src="/Users/shaoqiupan/Library/Application Support/typora-user-images/image-20210408113446465.png" alt="image-20210408113446465" style="zoom: 200%;" />





- 对于划分的单个元素，比如剩下8， 1 后 我们跳过divide1 和 divide2 使用merge3来进行处理

  ```python
  #sort1
  if len(nums[start:mid]) != 1:               #for the single number, if single, jump
    mergeSort(nums, start,mid)
  
    #very important
  if end == len(nums) - 1:                    #for the single number
     end = end + 1
      #sort2
  if len(nums[mid:end]) != 1:
        mergeSort(nums,mid, end)
      #merge3
   	merge(nums,start, mid, end)
  ```

- 一个函数负责划分

  ```python
          def mergeSort(nums, start, end):
              mid = (start + end) // 2
        # for situation only two numbers[3,-1]
              if (end - start <= 1):
                  if nums[start] > nums[end]:
                      temp = nums[start]
                      nums[start] = nums[end]
                      nums[end] = temp
                  return nums
              #sort1 
              #if for the single number, if single, jump
              if len(nums[start:mid]) != 1:               
                  mergeSort(nums, start,mid)
              
               #very important, for the last one
              if end == len(nums) - 1:                    
                  end = end + 1
              #sort2
              #if function for if single, jump
              if len(nums[mid:end]) != 1:
                  mergeSort(nums,mid, end)
  
              #merge3
              merge(nums,start, mid, end)
              nums = nums[start:end+1]
              return nums
  ```

- 一个函数负责merge

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
              return
          
  ```

  

- 学会画图来一步步跟踪， 每个递归都会开辟空间，理清思路(顺着管道走，有管道的地方优先走管道)

<img src="https://user-images.githubusercontent.com/37071362/114265464-7ad14500-9a23-11eb-8055-51dbe87de76a.png" alt="image-20210410171650786" style="zoom:40%;" />

------





### 本题难点：

- 分而治之

- 递归的思路比较绕，要画图理解
- end的判定条件，要清楚每一步切片后的array是多少，有没有重复，通过print时刻跟踪
- 判断什么时候divide， 什么时候跳过divide， divide的判定条件很重要，当只有一个数时，跳过divide，留着merge
- 当end处于最后一个，一定要记得end+1， 因为 nums[1,2,3] 对于 nums[2:3]是取不到3的，得nums[2:4]

