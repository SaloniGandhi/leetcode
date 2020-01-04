class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        minno=-2**31
        maxno=2**31 -1
        if x<0:
            flag=1
        result=[]
        xp=str(x)
        if flag==1:
            xp=xp[1:]
        xp=int(xp)
        while(xp):
            rem=xp%10
            result.append(rem)
            xp=xp//10
        #convert list of ints to the number
        no=0
        position=0
        for n in result:
            no+=n*pow(10,len(result)-1-position)
            position +=1
        if no not in range(minno, maxno):
            return 0
        if flag==1:
            return -1*no
        else:
            return no
            
        
        
        
                
    
        
