class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i<len(bits):
            if bits[i] == 1:
                if i == len(bits) - 2:
                    return False
                else:
                    i += 1
            elif bits[i] == 0:
                if i == len(bits) - 1:
                    return True
            i+=1
