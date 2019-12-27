class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # if not A:
        #     return None
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i
        return len(A)-1
