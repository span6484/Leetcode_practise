# 2. Add Two Numbers
* Question link https://leetcode.com/problems/add-two-numbers/
* [leetcode_2_AddTwoNumbers](./leetcode_2_AddTwoNumbers.py) 

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







### solution



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

