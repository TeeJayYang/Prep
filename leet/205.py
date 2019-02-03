class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
        mapping = {}
        for i in range(len(s)):
            if t[i] not in mapping:
                mapping[t[i]] = s[i]
            else:
                if mapping[t[i]] != s[i]:
                    return False
        return True
