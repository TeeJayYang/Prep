# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, sum):
        return (int(root.val == sum) + self.dfs(root.left, sum-root.val) + self.dfs(root.right, sum-root.val)) if root else 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.dfs(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) if root else 0

