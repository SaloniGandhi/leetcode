class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            front = i + 1
            rear = len(nums)-1    
            while front < rear:
                sum1 = nums[i] + nums[front] + nums[rear]
                if sum1 == 0:
                    res.append((nums[i],nums[front],nums[rear]))
                    while front < rear and nums[front] == nums[front+1]:
                        front += 1
                    while front < rear and nums[rear] == nums[rear-1]:
                        rear -= 1
                    front += 1
                    rear -= 1
                elif sum1 > 0:
                    rear -= 1
                else:
                    front += 1
        return res
