class Solution:
    def twoSumLessThanK(self, nums: List[int], K: int) -> int:
        arr=[]
        nums = sorted(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] < K:
                    arr.append(nums[i]+ nums[j])
                if nums[i]+ nums[j] >= K:
                    break
        if arr == []: 
          return -1
        return max(arr)
