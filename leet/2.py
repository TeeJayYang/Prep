# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def collectNumber(root):
            i = 0
            ret = 0
            while root:
                ret +=  root.val * (10 ** i)
                i += 1
                root = root.next
            return ret


        num1 = collectNumber(l1)
        num2 = collectNumber(l2)

        retSum = num1 + num2 


        # create return linked list
        if retSum == 0:
            return ListNode(0)
        ret = ListNode(int(retSum % 10))
        retSum //= 10
        root = ret
        while retSum != 0:
            ret.next = ListNode(int(retSum % 10))
            ret = ret.next
            retSum //= 10
        return root
