# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max = 0

        def dfs(node,depth):
            nonlocal max
            if not node:
                return
            if depth > max:
                max = depth
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        return max
