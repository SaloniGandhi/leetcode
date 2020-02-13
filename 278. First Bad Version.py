# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left=1
        right=n
        while(left<right):
            mid=left + (right-left)//2
            if isBadVersion(mid):
                right=mid
            elif isBadVersion(mid)==False:
                left=mid+1
        return right #return left also is fine since you in the end you are finding the bad version value
