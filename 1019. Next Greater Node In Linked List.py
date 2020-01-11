#Optimised solution
















#time limit exceeded solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return
        def maxvaluenode(temp1):
            m=temp1.val
            while(temp1):
                if temp1.val>m:
                    m=temp1.val
                    break
                temp1=temp1.next
            return m
        result=[]
        temp=head
        while(temp):
            x=maxvaluenode(temp)
            if x==temp.val:
                result.append(0)
            else:
                result.append(x)
            temp=temp.next
        return result
        
