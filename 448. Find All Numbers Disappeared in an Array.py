class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = set(nums)
        x = [i for i in range(1,len(nums)+1)]
        res = []
        for i in x:
            if i not in N:
                res.append(i)
        return res
