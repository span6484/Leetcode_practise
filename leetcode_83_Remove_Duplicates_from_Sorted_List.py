# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur != None and cur.next != None and cur.next.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        if cur != None and cur.next != None and cur.val == cur.next.val:
            cur.next = None
        return head