# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = []
        self.inorder(root,res)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
    
    def inorder(self,root,res):
        if not root:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
