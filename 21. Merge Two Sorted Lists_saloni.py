# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        left=l1
        right=l2
        prehead=ListNode(-1)
        prev=prehead
        while(l1 and l2):
            if l1.val<=l2.val:
                prev.next=l1
                l1=l1.next
            elif l2.val<l1.val:
                prev.next=l2
                l2=l2.next
            prev=prev.next
            
        if l1 is None:
            prev.next=l2
        else:
            prev.next=l1
        return prehead.next
