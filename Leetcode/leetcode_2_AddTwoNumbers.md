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