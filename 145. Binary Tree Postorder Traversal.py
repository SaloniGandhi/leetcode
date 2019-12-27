# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        if not root:
            return []
        else:
            result+=self.postorderTraversal(root.left)
            result+=self.postorderTraversal(root.right)
            result.append(root.val)
        return result
            
