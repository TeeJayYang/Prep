class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max3b4, max2b4, adj = 0,0,0
        for cur in nums:
            cur = max(max3b4 + cur, max2b4 + cur)
            max3b4, max2b4, adj = max2b4, adj, cur
        return max(max2b4, adj)
        """
        DP solution:
        moving summing window, max sum at current position
        can either be from 3 houses ago or 2 houses ago.
        """
