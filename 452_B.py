from lintcode.tools import get_chain
from lintcode.tools import random_chain
from lintcode.tools import new_chain

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):

        if head is None:
            return None

        p = head
        q = head.next

        while q is not None:
            if q.val == val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = p.next

        if head.val == val:
            head = head.next

        return head

list_val = [5]
head = new_chain(list_val)
x = Solution()
get_chain(head)
print("")
head2 = x.removeElements(head, 1)
get_chain(head2)

