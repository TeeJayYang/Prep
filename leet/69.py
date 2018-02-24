class Solution():
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # here you go interviewer
        # return int(x**0.5)

        # implementing binary search for root
        left, right = 1, x
        if x == 0:
            return 0
        while True:
            mid = (left + right)//2
            if mid > x/mid:
                right = mid -1
            else:
                if mid + 1 > x/(mid + 1):
                    return mid
                left = mid + 1
