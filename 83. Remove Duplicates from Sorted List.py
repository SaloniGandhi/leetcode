# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp=head
        if not head:
            return
        while(temp.next and temp):
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
                
               
        return head
