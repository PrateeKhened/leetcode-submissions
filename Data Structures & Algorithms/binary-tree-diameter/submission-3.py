# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def h(node):
            if not node:
                return 0 
            l = h(node.left)
            r = h(node.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        h(root)
        return self.res