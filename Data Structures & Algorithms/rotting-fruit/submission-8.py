class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        f = 0 
        t = 0 

        m, n = len(grid), len(grid[0])
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    f += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q and f > 0:
            
            for _ in range(len(q)):
                r, c = q.popleft() 

                for rf, cf in d:
                    rf, cf = r + rf, c + cf

                    if (0 <= rf < m and 0 <= cf < n and grid[rf][cf] == 1):
                        f -= 1
                        grid[rf][cf] = 2 
                        q.append((rf, cf))
            
            t += 1

        return t if f == 0 else -1