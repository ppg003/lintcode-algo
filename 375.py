class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        if root is None:
            return None
        new_root = TreeNode(root.val)
        if root.left is not None:
            new_root.left = self.cloneTree(root.left)
        if root.right is not None:
            new_root.right = self.cloneTree(root.right)
        return new_root