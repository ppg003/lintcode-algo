class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
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
