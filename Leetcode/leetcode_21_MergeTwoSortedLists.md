# 21. Merge Two Sorted Lists
**Easy**

Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:**

```
Input: l1 = [], l2 = [0]
Output: [0]
```

 

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.





解题思路：

1. 两两对比传入
2. 注意，在单个l1,l2 时候， 注意遇到最后一个时不要创建node



### Solution 1        --  11 对比，穿插传入								104 ms

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        l3 = ListNode()
        head = l3
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3.val = l1.val
                l1 = l1.next
            else:
                l3.val = l2.val
                l2 = l2.next
            l3.next = ListNode()
            l3 = l3.next
        
        while l1 != None:
            l3.val = l1.val
            l3.next = ListNode()
            if l1.next != None:
                l3.next = ListNode()
                l3 = l3.next
            l1 = l1.next
        while l2 != None:
            print(head)
            l3.val = l2.val
            if l2.next != None:
                l3.next = ListNode()
                l3 = l3.next
            l2 = l2.next
        print(head)
        l3.next = None
        return head
```





### **Solution2             接上list										**28 ms



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        head = dummy_head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                dummy_head.next = l1
                l1 = l1.next
            else:
                dummy_head.next = l2
                l2 = l2.next
            dummy_head = dummy_head.next
        if l1 != None:
            dummy_head.next = l1
            
        if l2 != None:
            dummy_head.next = l2
        return head.next
```

