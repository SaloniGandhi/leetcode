class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=sorted(stones)
        while(len(nums)>1):
            
            x=nums[-2]
            idx=nums.index(x)
            y=nums[-1]
            idy=nums.index(y)
            if x==y:
                nums.pop(idx)
                nums.pop(idy)
            else:
                nums[idy]=y-x
                nums.pop(idx)
                nums.sort()
                
        if nums:
            return nums[0]
        else:
            return 0
'''class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Swap the stone to be removed with the end.
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0'''
