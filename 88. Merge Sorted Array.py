class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iterations=max(len(nums1),len(nums2))
        k=0
        i=0
        j=0
        nums1_cp=nums1[:m]
        while(k<iterations):
            if j>len(nums2)-1:
                nums1[k]=nums1_cp[i]
                i+=1
            elif i >len(nums1_cp)-1:
                nums1[k]=nums2[j]
                j+=1
            elif nums1_cp[i]<nums2[j]:
                nums1[k]=nums1_cp[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            
