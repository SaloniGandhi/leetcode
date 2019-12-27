# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        sample=ListNode(0)
        sample.next=head
        temp=sample   
        while(temp.next!=None):
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return sample.next
            
