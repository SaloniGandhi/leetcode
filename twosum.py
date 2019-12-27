class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result=[]
        for i in range (0,len(nums)-1):
            value=target-nums[i]
            for j in nums[i+1:]:
                if value==j:
                    result.append(i)
                    result.append(nums[i+1:].index(j) + len(nums[:i+1]))
        return result
            
        
