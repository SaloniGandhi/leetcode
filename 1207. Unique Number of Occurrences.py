class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countdict={}
        for elem in arr:
            if elem not in countdict:
                countdict[elem]=1
            else:
                countdict[elem]+=1
        res=[]
        for k,v in countdict.items():
            if v not in res:
                res.append(v)
            else:
                return False
        return True
