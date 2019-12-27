# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMatch(self,s,t):
        if s and t:
            if s.val==t.val:
                return self.isMatch(s.left,t.left) and self.isMatch(s.right,t.right)
        return s is t            
   
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s:
            return False
        if self.isMatch(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
