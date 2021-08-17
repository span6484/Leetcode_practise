from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#version1: BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0
        if root == None:
            return level
        if root is not None:
            queue.append(root)
        while queue is not None:
            size = queue.__len__()
            if size == 0:
                break
            while size > 0:
                cur = queue.popleft()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)

                size -= 1

            level += 1
        return level

    
#version2: DFS
def dfs(root,num):
    if root == None:
        return num
    num += 1
    left = dfs(root.left, num)
    right = dfs(root.right,num)
    max_depth = max(left,right)
    return max_depth
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        num = 0
        max_depth = dfs(root,num)
        return max_depth
