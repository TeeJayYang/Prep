class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = []
        maxlen = 0
        for c in s:
            if c in substr:
                maxlen = max(len(substr), maxlen) 
                substr = substr[substr.index(c)+1:]
            substr.append(c)
            maxlen = max(len(substr), maxlen) 
        return maxlen
