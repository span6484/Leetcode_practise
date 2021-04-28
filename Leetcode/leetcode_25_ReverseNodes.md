# 25. Reverse Nodes in k-Group
**hard	**					2hs
Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.

*k* is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should remain as it is.

**Follow up:**

- Could you solve the problem in `O(1)` extra memory space?
- You may not alter the values in the list's nodes, only nodes itself may be changed.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Example 3:**

```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

**Example 4:**

```
Input: head = [1], k = 1
Output: [1]
```

 

**Constraints:**

- The number of nodes in the list is in the range `sz`.
- `1 <= sz <= 5000`
- `0 <= Node.val <= 1000`
- `1 <= k <= sz`

## 解题思路：

1. 先分析，k代表着每一组变化的长度
2. 判断有几组需要变化， 通过left， curr, right， old_head, new_head, old_end, new_end 几个指针来回调动指针方向
3. 注意第一次head 需要 = 第一个new_head, 剩下的是new_end -> old_end(new_head)
4. **画图**

| Time Submitted   | Status                                                       | Runtime | Memory  | Language |
| :--------------- | :----------------------------------------------------------- | :------ | :------ | :------- |
| 04/26/2021 13:19 | [Accepted](https://leetcode.com/submissions/detail/485309075/) | 40 ms   | 15.3 MB | python3  |

Solution:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head == None:
            return 
        old_head = head
        current = head
        new_head = None
        new_end = head
        c1 = head
        is_first = True
        
        #calculate len
        len_list = 0
        while c1 != None:
            len_list += 1
            c1 = c1.next
    
        if len_list == 1 or k == 1:
            return head
        times = len_list // k
        right = None
        for i in range(times):
            if right != None:
                old_head = right
                current = old_head
            right = None
            
            for j in range(k-1):
                left = current
                if right == None:
                    right = current.next
                current = right
                right = current.next
                current.next = left
            
            new_head = current
           # dertermine the head
            if is_first:
                head = new_head
                is_first = False
            else:
                new_end.next = new_head
                new_end = old_head
                current = right
        
        new_end.next = right
        return head
```

