        #works based on reference address of node and not value.. this is an address based solution.
        cache = set()
        while headA:
            cache.add(headA)
            headA = headA.next
        print(cache)  
        while headB:
            if headB in cache:
                return headB
            headB = headB.next
        
        return None
'''def findlen(thead):
            count=0
            while(thead):
                count+=1
                thead=thead.next
            return count
        
        alen=findlen(headA)
        blen=findlen(headB)
        if blen>alen:
            #blen is the longer list
            #let alen always be the standard bigger list
            headA,headB=headB,headA
            
        for i in range(abs(alen-blen)):
            headA=headA.next
        #brought it at the point where both these lists are now same
        while(headA is not headB and headA and headB):
            headB=headB.next
            headA=headA.next
        return headA
        '''
