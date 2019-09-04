# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 or l2):
            return l1
        ret = ListNode(0)
        i = ret
        while l1 or l2:
            if not l1:
                i.val = l2.val
                l2 = l2.next
            elif not l2:
                i.val = l1.val
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    i.val =  l1.val
                    l1 = l1.next
                else:
                    i.val = l2.val
                    l2 = l2.next
            if l1 or l2:
                i.next = ListNode(0)
                i = i.next
        return ret
