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
