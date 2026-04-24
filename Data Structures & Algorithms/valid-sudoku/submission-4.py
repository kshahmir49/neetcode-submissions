from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(9)}
        cols = {i:[] for i in range(9)}
        boxs = {(i,j):[] for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in rows.get(i,[None]) or board[i][j] in cols.get(j,[None]) or board[i][j] in boxs.get((i//3,j//3),[None]):
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                boxs[(i//3,j//3)].append(board[i][j])
        return True