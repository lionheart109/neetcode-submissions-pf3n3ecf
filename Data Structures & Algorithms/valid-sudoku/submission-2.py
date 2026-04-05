class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        cols = set()
        dappa = set()
        i = 0
        j = 0
        while i < 9 :
            while j < 9:
                if board[i][j] in row and board[i][j] !='.':
                    return False
                row.add(board[i][j])
                j+=1
            print(row)
            row.clear()
            i += 1
            j = 0
        print(i,j)
        i = 0
        j = 0
        while j < 9:
            while i < 9:
                if board[i][j] in cols and board[i][j] != '.':
                    return False
                cols.add(board[i][j])
                i+=1
            print(cols)
            cols.clear()
            j += 1
            i = 0
        i=0
        j=0
        while i < 9:
            while j < 9:
                if board[i][j]=='.':
                    j+=1
                    continue
                key = tuple((i//3,j//3,board[i][j]))
                if key in dappa:
                    return False
                dappa.add(key)
                j+=1
            j=0
            i+=1    
        return True


        