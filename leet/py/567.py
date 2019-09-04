class Solution:
    # check for for permuation of s1
    # is substring of s2
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = [0] * 26
        for c in s1:
            target[ord(c)-ord('a')] += 1
        window = [0] * 26

        for c in s2[:len(s1)]:
            window[ord(c)-ord('a')] += 1

        if window == target:
            return True

        for i in range(len(s1),len(s2)):
            window[ord(s2[i-len(s1)]) - ord('a')] -= 1 
            window[ord(s2[i]) - ord('a')] += 1
            if window == target:
                return True
        return False
