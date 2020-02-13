class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        pdt=1
        if not nums:
            return []
        #time limit exceeded for below
        # for i in range(len(nums)):
        #     pdt=1
        #     left=nums[:i]
        #     right=nums[i+1:]
        #     leftright=left+right
        #     for elem in leftright:
        #         pdt*=elem
        #     result.append(pdt)
        left=[]
        right=[1]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            left.append(pdt)
            pdt=pdt*nums[i]
        pdt=1
        for i in range(n-1,-1,-1):#iterate from behind
            right[i]=pdt
            pdt=pdt*nums[i]
        result=[left[i]*right[i] for i in range(len(left))]
        return result
            
                  
        
