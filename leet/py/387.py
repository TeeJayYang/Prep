class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occur = {}
        for each in s:
            occur[each] = occur.get(each,0) + 1
        for i in range(len(s)):
            if occur[s[i]] == 1:
                return i 
        return -1
