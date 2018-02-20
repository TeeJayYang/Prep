class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        def longsub(sa,sb):
            longest = 0
            tied = False
            for i in range(len(sa)):
                end = 0
                while end <= len(sa)-i:
                    subs = sa[i:i+end+1]
                    if subs not in sb:
                        if end > longest:
                            longest = end
                            tied = False
                        elif end == longest:
                            tied = True
                    end += 1
            return longest, tied

        l1, t1 = longsub(a,b)
        l2, t2 = longsub(b,a)
        # print ('{} {}\n{} {}'.format(l1, t1, l2, t2))
        if t1 and t2:
            return -1
        elif a  == b:
            return -1
        elif not t1 and not t2:
            return max(l1,l2)
        elif not t1 and t2:
            return l1
        elif not t2 and t1:
            return l2
        """
        correct solution is:
        def findLUSlength(self,A,B):
            if A == B:
                return -1
            return max(len(A),len(B))

        explanation:
            if len(A) > len(B) then the longest uncommon subsequence
            will be len(A) since B can't even be that length and thus cannot
            contain A
            if they are equal in length but not the same string then
            obviously longest uncommon length will be the either string's
            full length since they are not equal in value
            the only case left is if they are the same string, in which case
            there is no longest uncommon subsequence and thus the return value
            is -1
