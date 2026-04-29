class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def solve(i):
            if i >= len(cost):
                return 0

            cost_1_step = cost[i] + solve(i+1)
            cost_2_step = cost[i] + solve(i+2)

            return min(cost_1_step, cost_2_step)

        return min(solve(0), solve(1))