class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        r = [False] * m
        c = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r[i] = True
                    c[j] = True 
                
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i] or c[j]:
                    matrix[i][j] = 0