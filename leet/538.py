# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        s = 0 
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            nonlocal s
            s += node.val
            node.val = s
            dfs(node.left)
        dfs(root)
        return root
