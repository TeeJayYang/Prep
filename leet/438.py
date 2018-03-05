class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(s) < len(p):
            return ret
        sh = [0]*123
        ph = [0]*123
        # initial p hash population
        for i in p:
            ph[ord(i)] += 1
        # initial s hash population up until the length of p
        for i in s[:len(p)-1]:
            sh[ord(i)] += 1
        # iteration through s
        for i in range(len(p) - 1, len(s)):
            # each new letter is added to the hashmap counter
            sh[ord(s[i])] += 1
            # if the beginning of the substring window is greater than 0
            if i-len(p) >= 0:
                # subtract the leaving letter from the hashmap counter
                sh[ord(s[i-len(p)])] -= 1
            # if both the sliding window hashmap and the target string
            # hashmap are the same then success condition is reached
            if sh == ph:
                ret.append(i-len(p)+1)
        return ret
