class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:        

        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        
        maxLength = 0

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                right = dp[i][j + 1]
                down = dp[i + 1][j]
                diag = dp[i + 1][j + 1]

                sideLength = 0
                if matrix[i][j] == '1':
                    sideLength = 1 + min(right, down, diag)
                
                maxLength = max(maxLength, sideLength)
                dp[i][j] = sideLength
            
        return maxLength * maxLength
    
    