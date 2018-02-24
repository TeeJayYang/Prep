class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = sm = nums[0]
        for i in nums[1:]:
            sm = max(i, sm + i)
            mx = max(mx, sm)
        return mx
