from itertools import product
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes=0
        #rotten=[]
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]==2:
        #             rotten.append((i,j))
        #using list comprehension
        rotten=[(i,j) for i,j in product(range(len(grid)),range(len(grid[0]))) if grid[i][j]==2]
        fresh=sum(grid,[]).count(1)
        while fresh:
            if not rotten: #if rotten==[]
                return -1
            rotting=[]
            minutes+=1
            for i,j in rotten:
                for di,dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    #if the neighbours are one change them to 2
                    if  0<=di<len(grid) and 0<=dj<len(grid[0]) and grid[di][dj]==1:
                        grid[di][dj]=2
                        rotting.append((di,dj))
            fresh-=len(rotting)
            # minutes+=1
            rotten=rotting

        
        return minutes
                        
            
