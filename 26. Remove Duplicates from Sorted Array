class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1 
        #index represents where we would place our next unique element
        #index takes value 1 because we would return unique array elements with length atleast 1
        for i in range (len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[index]=nums[i+1]
                index+=1
        return index
        #it doesnt matter what elements are there beyond index
                
        
        # numsdict=dict()
        # if len(nums)==0:
        #     return
        # for num in nums:
        #     if num not in numsdict:
        #         numsdict[num]=1
        #     else:
        #         numsdict[num]+=1
        # numsdict={k:v for k,v in numsdict.items() if v>1}
        # #print(numsdict)
        # i=0
        # while(i<len(nums)):
        #     if nums[i] in numsdict:
        #         while()
        #         nums.remove(nums[i])
        #     else:
        #         i+=1
        # print(nums)
        # return len(nums)
