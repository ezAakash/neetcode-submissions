class Solution:
    def numSquares(self, n: int) -> int:
        dp = { 0 : 0 }
        for target in range(1, n + 1):
            dp[target] = target
            for s in range(1, target):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp.get(target - (square), 0))

        return dp[n]



       