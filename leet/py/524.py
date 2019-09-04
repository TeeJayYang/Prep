class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not s:
            return ''
        big_string = ''
        for each in d:
            if len(each) > s:
                continue
            else:
                i = 0
                for c in s:
                    if i < len(each) and each[i] == c:
                        i += 1
                if i == len(each):
                    if len(each) > len(big_string):
                        big_string = each
                    elif len(each) == len(big_string):
                        big_string = min(big_string, each)
        return big_string
