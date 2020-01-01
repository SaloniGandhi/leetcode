class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        for k,v in d.items():
            if v==1:
                return k
            
        
