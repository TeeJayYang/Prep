from random import randint

class Solution:

    ## high low is inclusive indicies
    def partition(self, nums, high, low):
        pivotIndex = randint(low, high)
        pivot = nums[pivotIndex]
        nums[high], nums[pivotIndex] = nums[pivotIndex], nums[high]
        smallI = low
        for i in range(low, high):
            if nums[i] <= pivot:
                nums[smallI], nums[i] = nums[i], nums[smallI]
                smallI += 1
        nums[smallI], nums[high] = nums[high], nums[smallI]
        return smallI

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low < high:
            pivI = self.partition(nums, high, low)
            if pivI < k:
                low = pivI + 1
            elif pivI > k:
                high = pivI - 1
            else:
                break
        return nums[k]

