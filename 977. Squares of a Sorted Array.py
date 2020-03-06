class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res=[]
        if not A:
            return
        for item in A:
            res.append(item*item)
        res=sorted(res)
        return res
        
