class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       #the only loop which helps us modify items in place is teh while loop because it will evaluate the len of the list everytime
            
       # for i in range(len(nums)-1):doesnt work!!
        i=0
        while(i<len(nums)):
            if nums[i]==val:
                nums.remove(nums[i])
                #update the nums length
            else:
                i+=1
            print(i)
                
        print (nums)
        return len(nums)
