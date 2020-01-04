class Solution:
    def myAtoi(self, str: str) -> int:
    #take a list which will hold all valid conversions
    #check if number is negative if yes maintain flag =1 while returning multiply *-1
    #convert digits in list to a number
        result=[]
        flag=0
        if str=="":
            return 0
        if str[0].isalpha():
            return 0
        #check if number is negative  and also appends char digits to my result list
        j=len(str)
        if not result:
            for i in range(len(str)):
                if i!=j-1:
                    if str[i]=='-' and str[i+1]==" ":
                        return 0
                if str[i]=='.':
                    break
                if str[i].isalpha():
                    break
                
                else:
                    if str[i].isdigit():
                        result.append(str[i])
                        print(result)
                        if i != j-1:
                            if not str[i+1].isdigit():
                                break
                        if str[i-1]=='-':
                            flag=1
                        if str[i-1]=='-' and str[i-2]=='+':
                            return 0
                        if str[i-1]=='+' and str[i-2]=='-':
                            return 0
        #now convert char numbers in result to int using position and ord
        
        number=0
        position=0
        for digit in result:
            #just convert character into int value using ord
            number+=(ord(digit)-ord('0'))*pow(10,len(result)-1-position)
            position+=1
        minnumber= -2**31
        maxno=2**31 -1
        print(number)
        if flag==1:
            return max(-1*number,minnumber)
        else:
            return min(number,maxno)
            
