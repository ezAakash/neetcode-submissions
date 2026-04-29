class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxLength = 0
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            nonlocal maxLength
            if i >= rows or j >= cols:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            diag = dfs(i + 1, j + 1)

            sideLength = 0
            if matrix[i][j] == '1':
                sideLength = 1 + min(right, down, diag)
            
            maxLength = max(maxLength, sideLength)
            memo[(i, j)] = sideLength
            return sideLength

        dfs(0, 0)
        
        return maxLength * maxLength