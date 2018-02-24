class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # its actually just fibonacci
        a = b = 1
        for i in range(n):
            a,b = b, a+b
        return a
