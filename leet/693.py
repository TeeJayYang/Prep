class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = "{:b}".format(n)
        digit = binary[0]
        for i in range(1,len(binary)):
                if digit == binary[i]:
                    return False
                digit = binary[i]
        return True

