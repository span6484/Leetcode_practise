# 2. Add Two Numbers
**median**                   用时40m

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

 

## 解题思路：

- 依次相加即可
- 注意两个细节，一个是不同的长度，第二个是进位，需要额外的1 加上去 







### solution(2nd)

```python
class Solution:
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0;
        dummy_head = ListNode(0);
        new_head = dummy_head
        
        while(l1 != None and l2 != None):
            val = l1.val + l2.val+carry
            carry = 0
            if(val > 9):
                val = val-10
                carry += 1
            
            new_head.next = ListNode(val)
            new_head = new_head.next
            l1 = l1.next
            l2 = l2.next
        
        
        rem_head = l1 if l1!=None else l2
        while(rem_head != None):
            val = rem_head.val+carry
            carry = 0
            if(val > 9):
                val = val-10
                carry += 1
            new_head.next = ListNode(val)
            new_head = new_head.next
            rem_head = rem_head.next

            
        if(carry != 0):
            new_head.next = ListNode(carry)
        return dummy_head.next
```



### Rick Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class SolutionRickImproved_2:
    # Note1: 进位叫做`carry`
    # Note2: 提炼出 add_helper
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        # h3: tail of return list
        h3 = dummy_head = ListNode(0)
        h1 = l1
        h2 = l2

        # 合并公共部分
        while h1 != None and h2 != None:
            digit_sum = h1.val + h2.val + carry
            
            h3,carry = self.add_helper(digit_sum, h3)

            h1 = h1.next
            h2 = h2.next

        # 合并剩余部分
        rem_head = h1 if h1 != None else h2
        while rem_head != None:
            digit_sum = rem_head.val+carry
            
            h3,carry = self.add_helper(digit_sum, h3)
            
            rem_head = rem_head.next
            
        if(carry != 0):
            h3.next = ListNode(carry)
            
        return dummy_head.next

    # add a node after h3
    def add_helper(self, val, h3):
        carry=0
        if(val >= 10):
            carry = 1
            newHead = ListNode(val-10)
        else:
            newHead = ListNode(val)
        h3.next = newHead
        return newHead, carry
```

