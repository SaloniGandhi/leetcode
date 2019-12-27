class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr = []
            for j in range(9):
                if board[i][j] != "." :
                        arr.append(board[i][j])
            if len(arr) != len(set(arr)):
                return False
        for j in range(9):
            arr = []
            for i in range(9):
                if board[i][j] != "." :
                        arr.append(board[i][j])
            if len(arr) != len(set(arr)):
                return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                arr = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y]!= "."]
                if len(arr) != len(set(arr)):
                    return False
       
        return True
