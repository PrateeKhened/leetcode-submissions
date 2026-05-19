class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() 
        posD = set()
        negD = set() 

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r=0):
            if r == n:
                copy = [''.join(row) for row in board] 
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r + c) in posD or (r - c) in negD:
                    continue 
                
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."
        
        dfs()
        return res