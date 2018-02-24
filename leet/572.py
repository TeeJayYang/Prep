class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        places = []
        def search(root, val):
            if not root:
                return
            if root.val == val:
                places.append(root)
            left = search(root.left, val)
            right = search(root.right, val)
        search(s, t.val)
        if not places:
            return False
        def compare(a, b):
            # a is the truth compared against b
            if not (a or b):
                return True
            elif (a and not b) or (b and not a):
                return False
            else:
                if a.val != b.val:
                    return False
                else:
                    return compare(a.left, b.left) and compare(a.right, b.right)
        for i in places:
            if compare(t, i):
                return True
        return False
        """
        explaination
        search() populates places with all possible starting locations
        of the root of the subtree, while compare() then actually compares
        two trees to see if they are the exact same
        """
