class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mx = mn = prices[0]
        d = 0
        for i in prices:
            if i > mx:
                mx = i
                if mx - mn > d:
                    d = mx - mn
            if i < mn:
                mn = i
                mx = i
        return d
