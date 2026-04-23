# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val 
        cnt = k 

        def traverse(node):
            nonlocal cnt, res 
            if node.left:
                traverse(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val 
                return 
            if node.right:
                traverse(node.right)
        
        traverse(root)
        return res