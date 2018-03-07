class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pidgeon hole principle
        # duplication must exist
        nums.sort()
        prev = None
        for i in nums:
            if i == prev:
                return i
            prev = i
    """
    using turtle and hare algorithm,
    by moving through the list using values
    as index, since there's duplication
    there must be a cycle in the "graph" but
    we cannot arrive at the start of the list
    since numbers start at 1
    """
    def findDuplicate(nums):
    slow = fast = finder = 0
    while True:
        # find meeting point
        print('{}:{}, {}:{}'.format(fast,nums[nums[fast]],slow,nums[slow]))
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            # once the meeting point has been found,
            # the meeting point and the start of the list
            # is equidistant to the entry point
            # (the duplicate number) 
            print('second round')
            # iterating from slow and from the start
            # at the same time will find the cycle entry
            # point when their values match
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
                print('{}:{}, {}:{}'.format(finder,nums[finder],slow,nums[slow]))
            return finder
