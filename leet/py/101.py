# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(a, b):
            # a is the left side and b is the right side
            if not(a and b):
                return a is b
            else:
                return (a.val == b.val) and compare(a.left, b.right) and compare(a.right, b.left)
        
        return compare(root.left, root.right) if root else True
