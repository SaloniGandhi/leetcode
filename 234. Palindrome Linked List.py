#recursion depth exceeded
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import*
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #reverse given singly linked list 
        #check if equal to given, if yes return True
        temp=deepcopy(head)
        if not head:
            return True
        
        prev=None
        curr=head
        nextn=None
        while(curr):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        print(prev)
        print(temp)
        while (prev and temp):
            if prev.val != temp.val:
                return False
            prev = prev.next
            temp = temp.next
        return True
        ########################################################################################
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import*
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #reverse given singly linked list 
        #check if equal to given, if yes return True
        '''
        temp=deepcopy(head)
        if not head:
            return True
        
        prev=None
        curr=head
        nextn=None
        while(curr):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        print(prev)
        print(temp)
        while (prev and temp):
            if prev.val != temp.val:
                return False
            prev = prev.next
            temp = temp.next
        return True
        '''
        def ffirsthalfend(head):
            fast=head
            slow=head
            while(fast.next and fast.next.next):
                fast=fast.next.next
                slow=slow.next
            return slow 
        def reverse(secondhalfstart):
            prev=None
            nextn=None
            curr=secondhalfstart
            while(curr):
                nextn=curr.next
                curr.next=prev
                prev=curr
                curr=nextn
            return prev
        if head is None:
            return True
        firsthalfend=ffirsthalfend(head)
        secondhalfstart=reverse(firsthalfend.next)
        result=True
        first=head
        second=secondhalfstart
        while(second and result):
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
            
        firsthalfend.next=reverse(secondhalfstart)
        
        return result
    
       
            
        
    
