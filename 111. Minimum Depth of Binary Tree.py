# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        mindepth=1
        level=[root]
        while(level):
            temp=[]
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if node.left==None and node.right==None:
                    return mindepth
            level=[]
            mindepth+=1
            for node in temp:
                level.append(node)
        return mindepth
                
