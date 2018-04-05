class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        if digits[0] != 9:
            digits[0] += 1
            digits.reverse()
            return digits
        carry = 0
        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1 
                carry = 0
                break
        if carry:
            digits.append(1)
        digits.reverse()
        return digits 
    
    # Alternatively,
    def plusOne2(self, digits):
        return map(int,list(str(int("".join(map(str, digits)))+1)))
