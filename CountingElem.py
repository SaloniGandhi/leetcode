class Solution:
    def countElements(self, arr: List[int]) -> int:
        if not arr:
            return
        numdict={}
        count=0
        for item in arr:
            if item not in numdict:
                numdict[item]=1
            else:
                numdict[item]+=1
        for i in range (len(arr)):
            prev=arr[i]-1
            if prev in numdict and numdict[prev]>0:
                count+=numdict[prev]
                numdict[prev]=0
        return count
            
