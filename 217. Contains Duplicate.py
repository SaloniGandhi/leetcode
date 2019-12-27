class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for i,val in d.items():
            if val > 1:
                return True
        return False
