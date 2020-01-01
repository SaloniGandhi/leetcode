class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''newarr=[]
        j=len(nums)-1
        while(k!=0):
            newarr[k-1]=nums[j]
            k-=1
            j-=1
        j=len(nums)-1
        p=0
        for i in newarr[j-k:]:
            if p==j-k+1:
                break
            else:
                newarr[i]=nums[p]
                p+=1
        print(newarr)
        return newarr
        '''
        #try reverse approach new array
        newarr=[0]*len(nums)
        j=len(nums)
        for i in range(len(nums)):
            newarr[(i+k)%j]=nums[i]
        for i in range(len(nums)):
            nums[i]=newarr[i]
        return newarr
        #reverse approach
        '''reverse entire list
        reverse first k elements
        reverse remaining n-k elements'''
        
        
        
