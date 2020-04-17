# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #case1 diameter passes through the root
    #case2: diameter doesnt pass through root  
        

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        
        ld=self.diameterOfBinaryTree(root.left)
        rd=self.diameterOfBinaryTree(root.right)
        
        return max(lh+rh,max(ld,rd))
        
    def maxDepth( self,root):
        if not root:
            return 0
        else:
            lh=self.maxDepth(root.left)
            rh=self.maxDepth(root.right)
            return 1+ max(lh,rh)
               
            
        
        
        
        
