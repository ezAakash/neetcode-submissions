class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def solve(i):
            if i >= len(cost):
                return 0

            return cost[i] + min(solve(i+1), solve(i+2))

        def solvedp():
            dp = [0] * (len(cost) + 1)
            dp[-2] = cost[-1]

            for i in range(len(dp) - 3 , -1, -1):
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
               
        return min(solve(0), solve(1))