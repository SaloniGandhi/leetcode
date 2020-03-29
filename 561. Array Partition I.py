class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        result=[]
        def make_pair(i,j):
            return min(i,j)
        for i in range(0,len(nums)-1,2):
            j=nums[i+1]
            i=nums[i]
            temp=make_pair(i,j)
            result.append(temp)
        print(result)
        return sum(result)        
