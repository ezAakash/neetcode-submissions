class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        memo = {}

        def dfs(r, prev_col):
            if r == m:
                return 0
            
            if (r, prev_col) in memo:
                return memo[(r, prev_col)]

            best = float('-inf')

            for col in range(n):
                cost = 0 if prev_col == -1 else abs(col - prev_col)
                best = max(
                    best,
                    points[r][col] - cost + dfs(r + 1, col)
                )

            memo[(r, prev_col)] = best
            return best

        return dfs(0, -1)
