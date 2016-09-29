"""
将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing

    def flatten(self, root):
        if root is None:
            return

        


