class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1]*len(nums)
        it = 1
        for i in range(len(nums)):
            ret[i] *= it
            it *= nums[i]
        it = 1
        for i in reversed(range(len(nums))):
            ret[i] *= it
            it *= nums[i]
        return ret
