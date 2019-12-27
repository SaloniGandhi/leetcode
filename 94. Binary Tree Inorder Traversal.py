# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        if not root:
            return []
        else:
            result=result+self.inorderTraversal(root.left)
            result.append(root.val)
            result=result+self.inorderTraversal(root.right)
        return result
    
   
