class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        a = set()
        def dfs(node):
            if not node:
                return False
            if k - node.val in a:
                return True
            else:
                a.add(node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)
