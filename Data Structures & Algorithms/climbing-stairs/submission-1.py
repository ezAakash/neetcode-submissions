class Solution:
    def climbStairs(self, stairs: int) -> int:
        
        def solvedp():
            dp = [0] * (stairs + 1)

            dp[-1] = dp[-2] = 1
            
            for i in range(len(dp) - 3, -1, -1):
                dp[i] = dp[i+1] + dp[i+2]

            return dp[0]

        return solvedp() #here i am defining the starting point .