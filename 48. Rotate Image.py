class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #for nxn matrix we would have n/2 cycles to complete
        #we go from outer boundry to the inner one
        # #x=boundry
        '''
        N=len(matrix)
        for i in range(N//2):
             #y=in the current square boundry we take 4 elems at a time
            for j in range(i,N-i-1):
                temp=matrix[i][j]
                matrix[i][j]=matrix[N-1-j][i]
                matrix[N-1-j][i]=matrix[N-1-i][N-1-j]
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i] 
                matrix[j][N-1-i]=temp
        return matrix
         '''
        
        
        
        #take transpose and reverse
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        print(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix
        
                
