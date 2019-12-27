class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if nums [-1] - nums[0] - len(nums) + 1 < k:
            return nums[-1] + k - (nums [-1] - nums[0] - len(nums) + 1) 
        missing = 0
        for i in range(1, len(nums)):
            temp = missing 
            missing += (nums[i] - nums[i-1] - 1)
            if k < missing:
                return nums[i-1] + k - temp
            elif k == missing :
                return nums[i-1] + k - temp
