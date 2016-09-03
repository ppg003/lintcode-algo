"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        if head is None or head.next is None:
            return head

        pre = None
        h = head
        cur = head
        while cur:
            h = cur
            cur = h.next
            tmp = pre
            h.next = tmp
            pre = h
        return h
