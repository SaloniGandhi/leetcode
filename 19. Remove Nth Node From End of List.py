# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        listlen=0
        if not head:
            return
        while(temp):
            listlen+=1
            temp=temp.next
        if listlen==1:
            return 
        targetindex=listlen-n+1
        print(targetindex)
        currentindex=1
        temp=head
        prev=temp
        while(currentindex!=targetindex):
            currentindex+=1
            prev=temp
            temp=temp.next
          
        prev.next=temp.next
        if temp==head:
            return head.next
        else:
            return head
        
