class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)
        lf=l1+l2
        i=0
        j=0
        med_array=[]
        if not nums1:
            if l2%2!=0:
                return nums2[l2//2]
            else:
                return (nums2[l2//2-1]+nums2[l2//2])/2.0
        if not nums2:
            if l1%2!=0:
                return nums1[l1//2]
            else:
                return (nums1[l1//2-1]+nums1[l1//2])/2.0
        for p in range(0,lf):
            if i>len(nums1)-1:
                med_array.append(nums2[j])
                j+=1
            elif j>len(nums2)-1:
                med_array.append(nums1[i])
                i+=1
            elif nums1[i]<=nums2[j]:
                med_array.append(nums1[i])
                i+=1
            elif nums2[j]<nums1[i]:
                med_array.append(nums2[j])
                j+=1
        print(med_array)
       
        if len(med_array)%2==0:
            #even numbered length array
            mid=(med_array[len(med_array)//2-1]+med_array[len(med_array)//2])/2.0
            
        else:
            mid=med_array[len(med_array)//2]
        return mid
