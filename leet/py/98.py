# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate(node, lowerlimit, upperlimit):
            if not node:
                return True
            if lowerlimit is not None and node.val <= lowerlimit:
                return False
            if upperlimit is not None and node.val >= upperlimit:
                return False
            return validate(node.left, lowerlimit, node.val) & validate(node.right, node.val, upperlimit)

        return validate(root, None, None)

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not (root.left or root.right):
            return True

        inOrder = []

        def inorderTraversal(node, nums):
            if not node:
                return
            inorderTraversal(node.left, nums)
            nums.append(node.val)
            inorderTraversal(node.right, nums)

        inorderTraversal(root, inOrder)

        prev = inOrder[0]
        for i in range(1, len(inOrder)):
            if inOrder[i] <= prev:
                return False
            prev = inOrder[i]
        return True
