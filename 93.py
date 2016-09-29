"""
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。
"""
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s\n"
)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        maxdepth = 1
        dl, dr = 0, 0
        if root.left is not None:
            dl = self.maxDepth(root.left)
        if root.right is not None:
            dr = self.maxDepth(root.right)
        max_d = max(dl, dr)
        return maxdepth + max_d

    def isBalanced(self, root):
        if root is None:
            return True
        dl, dr = 0, 0
        l_is_b, r_is_b = True, True
        if root.left is not None:
            dl = self.maxDepth(root.left)
            l_is_b = self.isBalanced(root.left)
        if root.right is not None:
            dr = self.maxDepth(root.right)
            r_is_b = self.isBalanced(root.right)
        # logging.debug("---------------------\n")
        # logging.debug("left depth : %s\n" % dl)
        # logging.debug("right depth : %s\n" % dr)
        # logging.debug("xxx : %s\n" % abs(dl - dr))
        # logging.debug("---------------------\n")
        if abs(dl - dr) < 2 and l_is_b and r_is_b:
            return True
        return False