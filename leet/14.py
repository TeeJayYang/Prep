class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for i in strs[1:]:
            minlen = min(len(prefix), len(i))
            if len(prefix) > minlen:
                prefix = prefix[:minlen]
            for c in range(minlen):
                if prefix[c] != i[c]:
                    prefix = prefix[:c]
                    break
        return prefix
