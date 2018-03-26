# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        gc.collect()
        runnerA = headA
        runnerB = headB
        while runnerA is not runnerB:
            runnerA = runnerA.next if runnerA else headA
            runnerB = runnerB.next if runnerB else headB
        return runnerA
