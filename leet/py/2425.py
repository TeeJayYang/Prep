class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        temp1 = 0
        temp2 = 0
        if len(nums1) % 2 == 1:
            temp2 = reduce(operator.xor, nums2)
        if len(nums2) % 2 == 1:
            temp1 = reduce(operator.xor, nums1)
        return temp2 ^ temp1
