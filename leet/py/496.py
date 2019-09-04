class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2d = {}
        for i in range(len(nums2)):
            nums2d[nums2[i]] = i
        ret = []
        for i in nums1:
            for j in range(nums2d[i],len(nums2)):
                if nums2[j] > i:
                    ret.append(nums2[j])
                    break
                if j == len(nums2)-1:
                    ret.append(-1)
        return ret

