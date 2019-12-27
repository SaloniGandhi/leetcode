# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count=1
        if not head:
            return
        #compute the len of ll
        temp=head
        while(temp.next!=None):
            count+=1
            temp=temp.next
        print(count)
        if count%2==0:
            midindex=((count-1)//2)+1
        else:
            midindex=(count-1)//2
        print(midindex)
        temp=head
        cntindex=0
        while(temp.next!=None):
            if cntindex == midindex:
                break
            else:
                cntindex+=1
                temp=temp.next
        return temp
        
