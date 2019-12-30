class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        def nextnode(n):
            tsum=0
            while(n>0):
                digit=n%10
                tsum+=digit**2
                n=n//10
            return tsum
        
        t=n #t=19
        r=nextnode(nextnode(n)) #r=68
        while (t!=r and t!=1):
            t=nextnode(t)
            r=nextnode(nextnode(r))
            
        if t==1:
            return True
        else:
            return False
            
            
        
       
            
