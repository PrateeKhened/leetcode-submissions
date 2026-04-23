# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0 
        def helper(node, maxx):
            if not node:
                return None 
            if node.val >= maxx:
                self.count += 1
                maxx = node.val
            if node.left:
                helper(node.left, maxx)
            if node.right:
                helper(node.right, maxx)
        helper(root, root.val)
        return self.count 