class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums) - 1
        
        dp = [N] * (N + 1)
        dp[-1] = 0

        for i in range(N - 1, -1, -1):
            end = min(N + 1, i + nums[i] + 1)
            curr_min = dp[i]
            for j in range(i+1, end):
                curr_min = min(curr_min, dp[j])
            
            dp[i] = 1 + curr_min
        
        return dp[0]

            
             