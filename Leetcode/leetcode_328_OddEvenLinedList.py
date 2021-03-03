# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        if head.next == None:
            return head
        
        l1_odd = ListNode()
        
        l2_even = ListNode()
        
        l1_head = l1_odd
        l2_head = l2_even
        
        state = 1
        while head != None:
            if(state == 1):
                l1_head.next = head
                head = head.next
                l1_head = l1_head.next
                state = 0
            if(state == 0):
                l2_head.next = head
                if(head != None and head.next != None):
                    head = head.next
                    l2_head = l2_head.next
                    state = 1
                else:
                    l2_head = head
                    break
                
        l1_head.next = l2_even.next
        return l1_odd.next
    