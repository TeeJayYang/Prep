# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tortoise = hare = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare is tortoise:
                return True
        return False
        """
        explaination:
        tortoise and hare algorithm,
        two runners, one doing a single step at a time
        and the second one doing two steps at a time.
        If there is loop then they will meet, otherwise 
        they will reach the end of the sequence.
        """
