# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        result=[]
        while(temp):
            result.append(temp.val)
            temp=temp.next
        number=0
        position=0
        for i in reversed(result):
            number+=i*pow(2,position)
            position+=1
        return number
            
        
