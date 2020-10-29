"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        dic = {}
        
        cur = head
        
        while(cur != None):
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while(cur != None):
            if(cur.next != None):
                dic[cur].next = dic[cur.next]
            if(cur.random == None):
                dic[cur].random = None
            
            else:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]