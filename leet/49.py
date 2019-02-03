from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            d[tuple(chars)].append(s)
        
        return [v for k,v in d.items()] 
