# -*- coding:utf-8 -*-
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_chain(head):
    print(head.val, end="")
    next_node = head.next
    while next_node is not None:
        print(" -> " + str(next_node.val), end="")
        next_node = next_node.next

    print(" -> " + str(next_node), end="")


def random_chain(length, min, max):
    if length == 0:
        return None

    head = ListNode(random.randint(min, max))
    this_node = head

    for i in range(length - 1):
        next_node = ListNode(random.randint(min, max))
        this_node.next = next_node
        this_node = next_node

    this_node.next = None

    return head


def new_chain(list_val):
    if not list_val:
        return None

    head = ListNode(list_val[0])
    this_node = head

    for i in range(1, len(list_val)):
        next_node = ListNode(list_val[i])
        this_node.next = next_node
        this_node = next_node

    this_node.next = None

    return head
