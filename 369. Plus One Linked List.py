# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def r(head):
            curr=head
            prev=None
            nextn=None
            while(curr):
                nextn=curr.next
                curr.next=prev
                prev=curr
                curr=nextn
            return prev
        t=ListNode(1)
        temp1=head
        if temp1.next==None and temp1.val==9:
            temp1.val=0
            temp1.next=t
            temp1=r(temp1)
            return temp1
        elif temp1.next==None and temp1.val<9:
            temp1.val+=1
            return temp1
        else:
            l=prev=r(head)
            carry=1
            flag=0
            while(l): 
                if l.val==9 and flag==0:
                    carry=1
                    l.val=0
                    if l.next==None and flag==0:
                        l.next=t
                        q=r(prev)
                        return q
                else:
                    l.val=l.val+carry
                    flag=1
                    carry=0
                l=l.next
            l=r(prev)
            return l
            
        
    
