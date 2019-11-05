# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
# [1,1,1,1,2]    val = 1 
        while head.val == val:
            if head.next == None:
                return
            head = head.next
        cur = head
    
        while cur.next != None:
            if cur.next.val == val and cur.next.next != None:
                cur.next = cur.next.next
                continue
            if cur.next.val == val and cur.next.next == None:
                cur.next = None
                break
            cur = cur.next
        return head