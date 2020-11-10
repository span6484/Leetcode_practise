# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
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
            
        return start.next
        