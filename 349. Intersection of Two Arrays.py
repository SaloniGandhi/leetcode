  class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        a = set(nums1)
        b = set(nums2)
        res = []
        for i in a:
            if i in b:
                res.append(i)
        return res
