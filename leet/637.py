# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode 
        :rtype: List[float]
        """
        l = []
        def dfs(node, depth = 0):
            if node:
                if len(l) == depth:
                    l.append([0,0])
                l[depth][0] += node.val
                l[depth][1] += 1
                dfs(node.left,depth+1)
                dfs(node.right,depth+1)
        dfs(root)
        return[s/float(c) for s,c in l]

