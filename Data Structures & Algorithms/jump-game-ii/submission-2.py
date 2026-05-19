class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [N] * N
        dp[-1] = 0

        for i in range(N - 2, -1, -1):
            end = min(N, i + nums[i] + 1)
            for j in range(i+1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]

            
             