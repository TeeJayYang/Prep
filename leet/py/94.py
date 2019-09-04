# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # fuck doing it iteratively
        ret = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            ret.append(root.val)
            traverse(root.right)
        traverse(root)
        return ret
