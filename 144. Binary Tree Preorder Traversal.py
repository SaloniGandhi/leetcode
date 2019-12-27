# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        result=[]
        if not root:
            return []
        result.append(root.val)
        result+=self.preorderTraversal(root.left)
        result+=self.preorderTraversal(root.right)
        return result
