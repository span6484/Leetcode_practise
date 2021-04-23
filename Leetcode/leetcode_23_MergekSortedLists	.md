# 23. Merge k Sorted Lists								

**Hard**

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*            ATTENTION: COMPOLEXITY

 

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```



思路：

**divde and conquer**

做这道题**错误**思路用穿插着做， 因为最后一个测试是一个庞大的数组

正确思路用分治算法， 将array不断二分，再两两合并，值得注意的是， 可以将每次合并出来的list都存储到list[start]上，不断递归并最终返回 list[start]

<img src="https://user-images.githubusercontent.com/37071362/115814142-10f36b00-a427-11eb-8e11-9c5059e3e3f9.png" alt="image" style="zoom:50%;" />



# Solution	

Runtime: 128 ms, faster than 32.98% of Python3 online submissions for Merge k Sorted Lists.

Memory Usage: 17.8 MB, less than 65.52% of Python3 online submissions for Merge k Sorted Lists.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(len(lists) == 0):
            return None
        if len(lists) == 1:
            return lists[0]
        def merge(lists, start, end):
            lists1 = lists[start]
            lists2 = lists[end]
            dummy_head = ListNode(0)
            head = dummy_head
            while lists1 != None and lists2 != None:
                if lists1.val <= lists2.val:
                    dummy_head.next = lists1
                    lists1 = lists1.next
                else:
                    dummy_head.next = lists2
                    lists2 = lists2.next
                dummy_head = dummy_head.next
            if lists1 != None:
                dummy_head.next = lists1
            else:
                dummy_head.next = lists2
            lists[start] = head.next
            return
        def divide(lists,start, end):
            mid = (start+end) // 2
            if mid - start > 2:
                divide(lists, start, mid)
            if mid - start == 2:
                merge(lists, start,mid-1)
            if end - mid > 2:
                divide(lists, mid, end)
            if end - mid == 2:
                merge(lists,mid, end-1)
            merge(lists,start, mid)
            return lists[start]
        divide(lists, 0, len(lists))
        return lists[0]
```





## failed solution 																O(n)			

​																																							132/133

```python
#尝试穿插，想要不占内存的解法可惜失败了， 能过除了最后最多测试的解法, 对比3个让dummy指向，当为空的是仅退出

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
				# for [[]], [], elminate none
        if(len(lists) == 0):
            return None
        i = 0
        while i < len(lists):
          if lists[i] == None:
            lists.pop(i)
            i = 0
          i += 1
        lists = arr
        None_time = 0
        for i in lists:
            if i == None:
                None_time += 1
        if None_time == len(lists):
            return None
        if len(lists) == 1:
            return lists[0]
          
          
        def isSmaller(a,b):
            if a < b:
                return True
            return False
        dummy_node = ListNode()
        head = dummy_node
        i = 0
        temp = None
        index = None
        while len(lists) > 1:
            if temp == None:
                temp = lists[i].val
                index = i
                i += 1
                continue
            if isSmaller(lists[i].val, temp):
                temp = lists[i].val
                index = i
            if i == len(lists) - 1:
                dummy_node.next = lists[index]
                dummy_node = dummy_node.next
                lists[index] = lists[index].next
                #pop when none
                if lists[index] == None:
                    lists.pop(index)
                temp = None
                i = 0
                continue       
            i += 1
        dummy_node.next = lists[0]
        return head.next
```



## BUG

1. 

```python
In [1]: for i in range(0,3,1):
   ...:     if i == 2:
   ...:         i = 0
   ...:     print(i)
```

Output:         why not reset the function i like while

```
0
1
0
```

2. Pop 跳过重复问题

```
input: [[0,1,2],[-10,-8,-5,-4],[],[],[-3],[-10,-9,-6,-4,-3,-2,-2,-1,2],[-9,-9,-2,-1,0,1],[-9,-4,-3,-2,2,2,3,3,4]]
```



wrong 

```python
while i < len(lists):
  if lists[i] == None:
  lists.pop(i)
i += 1
```



pop后需要重置下

correct

```
while i < len(lists):
  if lists[i] == None:
  lists.pop(i)
  i = 0
i += 1
```


