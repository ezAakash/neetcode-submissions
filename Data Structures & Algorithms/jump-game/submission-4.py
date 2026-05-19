class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)

        dp = [False] * (N)
        dp[-1] = True

        for i in range(N - 2, -1, -1):
            for jump in range(i+1, min(N, i + nums[i] + 1)):
                if dp[jump]:
                    dp[i] = True
                    break
        
        return dp[0]

        
