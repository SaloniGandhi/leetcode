class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        for n in digits:
            num+=str(n)
        num=int(num)
        s=1+num
        s=str(s)
        result=[]
        for i in s:
            result.append(int(i))
        print(result)
        
        return result
        num=0
        position=0
        for digit in digits:
            num+=digit*pow(10,len(digits)-1-position)
            position+=1
        num=num+1
        return [int(i) for i in str(num)]
