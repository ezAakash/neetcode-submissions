class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums) - 1
        
        dp = [N] * (N + 1)
        dp[-1] = 0

        for i in range(N - 1, -1, -1):
            if i + nums[i] > N:
                dp[i] = 1 + min(dp[N], dp[i + 1])
            else:
                dp[i] = 1 + min(dp[i + nums[i]], dp[i + 1])
        
        return dp[0]

            
             