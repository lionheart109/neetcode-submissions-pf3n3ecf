class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        cols = set()
        dappa = set()
        i = 0
        j = 0
        while i < 9 :
            while j < 9:
                key = tuple((i//3,j//3,board[i][j]))
                if (board[i][j]!='.' and board[i][j] in row)or(board[j][i]!='.' and board[j][i] in cols) or (board[i][j]!='.' and key in dappa):
                    return False                  
                row.add(board[i][j])
                cols.add(board[j][i])
                dappa.add(key)
                j+=1
            row.clear()
            cols.clear()
            i += 1
            j = 0
        return True