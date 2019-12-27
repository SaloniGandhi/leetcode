# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         ans=[]
#         level = [root]
#         while level:
#             ans.append([node.val for node in level])
#             temp = []
#             for node in level:
#                 if node.left:
#                     temp.append(node.left)
#                 if node.right:
#                     temp.append(node.right)
#             level = []
#             for node in temp:
#                 level.append(node)
           
#         return ans
        if not root:
            return []
        result=[]
        level=[root]
        while level:
            temp=[]
            result.append([node.val for node in level])
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=[]
            for node in temp:
                level.append(node)
        return result
