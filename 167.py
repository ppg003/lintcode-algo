from lintcode.tools import get_chain
from lintcode.tools import new_chain


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):

        if l1 is None and l2 is None:
            return None

        if l1 is not None and l2 is None:
            return l1

        if l2 is not None and l1 is None:
            return l2

        head = ListNode(0)
        p_res = head
        p_1 = l1
        p_2 = l2

        cache_next = 0
        while p_1 is not None and p_2 is not None:
            sum = p_1.val + p_2.val + cache_next
            if sum >= 10:
                cache_next = 1
                sum -= 10
            else:
                cache_next = 0
            p_res.val = sum

            if p_1.next is not None and p_2.next is not None:
                p_res.next = ListNode(0)
                p_res = p_res.next
            p_1 = p_1.next
            p_2 = p_2.next

        if p_1 is None and p_2 is None:
            if cache_next != 0:
                p_res.next = ListNode(0)
                p_res = p_res.next
                p_res.val = 1
            return head

        if p_1 is None:
            p_res.next = ListNode(0)
            p_res = p_res.next
            while p_2 is not None:
                sum = p_2.val + cache_next
                if sum >= 10:
                    cache_next = 1
                    sum -= 10
                else:
                    cache_next = 0
                p_res.val = sum
                if p_2.next is not None:
                    p_res.next = ListNode(0)
                    p_res = p_res.next
                p_2 = p_2.next

            return head

        if p_2 is None:
            p_res.next = ListNode(0)
            p_res = p_res.next
            while p_1 is not None:
                sum = p_1.val + cache_next
                if sum >= 10:
                    cache_next = 1
                    sum -= 10
                else:
                    cache_next = 0
                p_res.val = sum
                if p_1.next is not None:
                    p_res.next = ListNode(0)
                    p_res = p_res.next
                p_1 = p_1.next

            return head


n1 = [3, 1, 7]
n2 = [5, 9, 2, 1, 5]
l1 = new_chain(n1)
l2 = new_chain(n2)
x = Solution()

get_chain(l1)
print("")
get_chain(l2)
print("")

lr = x.addLists(l1, l2)
get_chain(lr)
