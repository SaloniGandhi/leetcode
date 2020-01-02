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
            
