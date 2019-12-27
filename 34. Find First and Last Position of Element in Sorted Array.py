class Solution:
    def binarysearchleftorright(self,nums,target,boolleft):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if boolleft:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
        if boolleft:
            return low
        else:
            return high
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = (self.binarysearchleftorright(nums,target,True),self.binarysearchleftorright(nums,target,False))
        if res[0] <= res[1]:
            return res
        return [-1,-1]
