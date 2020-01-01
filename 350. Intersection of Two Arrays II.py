class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        numd={}
        for i in nums1:
            if i not in numd:
                numd[i]=1
            else:
                numd[i]+=1
        print(numd)
        for e in nums2:
            if e in numd:
                numd[e]-=1
                if numd[e]>=0:
                    result.append(e)
                    
            else:
                continue
        
        
        
        return result
