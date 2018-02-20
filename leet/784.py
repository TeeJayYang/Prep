class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret = set()
        ret.add(S)
        def foo(s,i):
            # i is index
            upper = lower = s
            if i == len(s):
                return
            if S[i].isalpha():
                upper = s[:i]+s[i].upper()+s[i+1:]
                lower = s[:i]+s[i].lower()+s[i+1:]
            ret.add(upper)
            ret.add(lower)
            foo(upper,i+1)
            foo(lower,i+1)
        foo(S,0)
        return list(ret)
## non recursive solution
class Solution:
    def letterCasePermutation(self, S):
	res = ['']
	for ch in S:
	    if ch.isalpha():
		res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
	    else:
		res = [i+ch for i in res]
	return res
