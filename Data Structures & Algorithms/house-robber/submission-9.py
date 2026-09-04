class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums) + 1)
        def dpSolve():
            dp[-2] = nums[-1] # Base case here turned into initialization

            for i in range(len(dp) - 3, -1, -1): #don't do this mistake again , we use dp for iteration not the original array cause this definition keep the track of the original array perfectly too. 
                rob = nums[i] + dp[i+2]
                skip = dp[i+1]

                dp[i] = max(rob, skip)

            return dp[0]
        
        print(dp)
        return dpSolve()
        
