# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        serRes = [str(root.val)]
        q = deque([root])
        while q:
                node = q.popleft() 
                if not node:
                    continue
                serRes.append(str(node.left.val) if node.left else "None") 
                serRes.append(str(node.right.val) if node.right else "None")
                q.append(node.left)
                q.append(node.right)

        while serRes and serRes[-1] == "None":
            serRes.pop() 

        return " ".join(serRes)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or len(data) == 0:
            return None


        vals =  data.split() 
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft() 

            if i < len(vals) and vals[i] != "None":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
        
            if i < len(vals) and vals[i] != "None":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))