# 做题思路： 通过question2， 我们拥有了相加的方法，我们将list反转变成question2类型， 然后返回的list也再次反转
![leetcode_445_submission](https://user-images.githubusercontent.com/37071362/98677241-de8e0e00-23b0-11eb-8cd0-56cfb9a7abce.PNG)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

# 反转list1
        tail = None
        head1 = l1
        
        while head1 != None:
            l1 = head1
            head1 = head1.next
            l1.next = tail
            tail = l1

            
# 反转list2            
        tail = None
        head1 = l2
        
        while head1 != None:
            l2 = head1
            head1 = head1.next
            l2.next = tail
            tail = l2
        
        
        # question2's method
        temp = 0
        newHead = ListNode(0)
        start = newHead
        h1 = l1
        h2 = l2
        
        while h1 != None and h2 != None:
            val = h1.val + h2.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
                
            h1 = h1.next
            h2 = h2.next
            
        while h1 != None:
            val = h1.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
            
            h1 = h1.next
 
        while h2 != None:
            val = h2.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
            
            h2= h2.next
            
        if(temp != 0):
            
            h3 = newHead
            newHead = ListNode(temp)
            h3.next = newHead

        # 反转返回的list， 在question2里应该返回start.next
        tail = None
        head1 = start.next
        
        while head1 != None:
            start.next = head1
            head1 = head1.next
            start.next.next = tail
            tail = start.next
            
        return start.next
        
