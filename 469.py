
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        if a is None and b is not None:
            return False
        if a is not None and b is None:
            return False
        if a is None and b is None:
            return True
        if a.val != b.val:
            return False

        if not(a.left is not None and b.left is not None):
            if a.left is None and b.left is None:
                pass
            else:
                return False
        else:
            if not self.isIdentical(a.left, b.left):
                return False

        if not (a.right is not None and b.right is not None):
            if a.right is None and b.right is None:
                pass
            else:
                return False
        else:
            if not self.isIdentical(a.right, b.right):
                return False
        return True



















