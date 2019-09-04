class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                ret += diff 
        return ret
