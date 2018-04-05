class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numbers = set()
        while n != 1:
            squareSum = sum(int(i)**2 for i in str(n))
            if squareSum in numbers:
                return False
            else:
                numbers.add(squareSum)
            n = squareSum
        return True
