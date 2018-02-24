class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = [i.lower() for i in s if i.isalnum()]
        return l == list(reversed(l))
