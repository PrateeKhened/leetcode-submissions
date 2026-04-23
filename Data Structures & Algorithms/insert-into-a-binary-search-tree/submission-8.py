# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if root is None:
            return new 
        temp = root 
        while temp:
            if new.val > temp.val:
                if temp.right is None:
                    temp.right = new 
                    return root 
                temp = temp.right 
            else:
                if temp.left is None:
                    temp.left = new 
                    return root 
                temp = temp.left 
                