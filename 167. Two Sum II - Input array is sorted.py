class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for index,val in enumerate(numbers):
            if target - val in d:
                return (d[target-val]+1,index+1)
            d[val] = index
        
