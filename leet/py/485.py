class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > max:
                    max = count
                count = 0
            else:
                count += 1
        if count > max:
            max = count
        return max
