# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start_idx=m
        end_idx=n
        prev = dummy=ListNode(0)
        dummy.next=head
        # curr = head
        # count = 0
        # while curr:
        #     count += 1
        #     if count == m :
        #         head1 = curr
        #         prev1 = prev
        #     if count == n:
        #         head2 = curr
        #         temp = curr.next
        #         head2.next = None
        #         break
        #     prev = curr
        #     curr = curr.next
        # previous = None
        # while head1 :
        #     current = head1
        #     head1 = head1.next
        #     current.next = previous
        #     previous = current
        # prev1.next = previous
        # curr = head
        # while curr.next:
        #     curr = curr.next
        # curr.next = temp
        # return dummy.next
        if not head:
            return
        if m==n:
            return head
        for i in range(1,start_idx):
            prev=prev.next
        # print(prev.val)
        # print(prev.next.val)
        #make previous point to 1 before thes startidx
        curr=prev.next
        while(start_idx<end_idx):
            #start reversing these
            #print (head)
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
            start_idx+=1
        
        return dummy.next
        
