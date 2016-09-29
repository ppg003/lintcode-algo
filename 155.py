class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def minDepth(self, root):
        if root is None:
            return 0
        d = 1
        if root.left is not None and root.right is not None:
            dl, dr = 0, 0
            if root.left is not None:
                dl = self.minDepth(root.left)
            if root.right is not None:
                dr = self.minDepth(root.right)
            d_min = min(dl, dr)
            return d_min + d
        elif root.left is None:
            return self.minDepth(root.right) + d
        else:
            return self.minDepth(root.left) + d

