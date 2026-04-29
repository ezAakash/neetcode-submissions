class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solvedp(nums):
            dp = [0] * (len(nums) + 1)


            dp[-2] = nums[-1]
            for i in range(len(dp) - 3, -1, -1):
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])

            return dp[0]

        return max(solvedp(nums[1:]), solvedp(nums[:-1]))