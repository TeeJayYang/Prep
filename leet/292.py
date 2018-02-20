class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
        
        """
        you will lose if the number of stones
        in the nim game is a multiple of 4
        can be proved by natural induction
        base case: n = 4, no matter what you remove,
            the opponent can always remove the last stone
        induction hypothesis: 4k will lose for k is int
            when you go first
        induction step: 4(k+1) = 4k + 4, no matter what
            you remove, opponent can force the next turn
            for you to remove starting at 4k, which you
            will lose
        """
