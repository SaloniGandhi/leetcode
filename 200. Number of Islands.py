class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count_islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.check_neighbour(i,j,grid)
                    count_islands+=1
        return count_islands
    
    def check_neighbour(self,i,j,grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return            
        else:
            grid[i][j]='#'
            self.check_neighbour(i,j+1,grid)
            self.check_neighbour(i,j-1,grid)
            self.check_neighbour(i+1,j,grid)
            self.check_neighbour(i-1,j,grid)
            
                        
