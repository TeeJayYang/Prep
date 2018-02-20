class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        w = word
        return w == w.lower() or w == w.upper() or w == w.title()
