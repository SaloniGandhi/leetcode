class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        #index consists of the location in the array where we would place a non zero number
        #index location gets updated in every iteration to determine the next non zero which would come at index
        for i in range(len( nums)):
            if nums[i] != 0:
                nums[index],nums[i]=nums[i],nums[index]#swap nums[i] with nums[index]
                index+=1
                print(nums)
       
    
    
#         end=len(nums)-1
#         start=index
#         #how to write a for loop for this task
#         while(start<=end):
#             nums[start]=0
#             start+=1
#         print(nums)
        
        return nums
    
