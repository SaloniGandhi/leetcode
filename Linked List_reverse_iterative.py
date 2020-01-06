 #solution to reverse a linked list iteratively
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        nextn=None
        curr=head
        while(curr):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        return prev
            
        
            
        
        
