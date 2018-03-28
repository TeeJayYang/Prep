# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return []
        ret = [intervals[0]]
        for each in intervals:
            if each.start <= ret[-1].end:
                ret[-1] = Interval(ret[-1].start, max(each.end, ret[-1].end))
            else:
                ret.append(each)
        return ret
