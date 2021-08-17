from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        queue = deque()
        level_cb = list()
        queue.append(root)
        while queue:
            level = list()
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    level.append(cur.val)
            if level:
                level_cb.append(level)
        return level_cb
