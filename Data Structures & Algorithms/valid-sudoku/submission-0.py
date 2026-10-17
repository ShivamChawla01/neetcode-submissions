class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(board)):
            if(i>=0 and i<3):
                row = 0
            elif(i>=3 and i<6):
                row = 1
            else:
                row = 2
            for j in range(len(board[0])):
                if(board[i][j] == "."):
                    continue
                if(j>=0 and j<3):
                    col = 0
                elif(j>=3 and j<6):
                    col = 1
                else:
                    col = 2

                d[board[i][j]].append("r:"+str(i))
                d[board[i][j]].append("c:"+str(j))
                d[board[i][j]].append("row: "+str(row)+"col: "+str(col))
        for i in d:
            if(len(d[i]) != len(set(d[i]))):
                return False
        return True

        