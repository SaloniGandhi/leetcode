class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check every row in board
        for i in range(0,9):
            arr=[]
            for j in range(0,9):
                if board[i][j]!='.':
                    arr.append(board[i][j])
            if len(set(arr))!=len(arr):
                return False
        #check for every column in board
        for j in range(9):
            arr=[]
            for i in range(9):
                if board[i][j]!='.':
                    arr.append(board[i][j])
            if len(set(arr))!=len(arr):
                return False
        #for grid start values taken will be 0,3,6 by i and j
        for i in (0,3,6):
            for j in (0,3,6):
                arr=[board[x][y] for x in range(i,i+3) for y in range(j,j+3) if board[x][y]!='.']
                
                if len(set(arr))!=len(arr):
                    return False
        return True
                
