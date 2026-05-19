class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)

        reach = 0

        for i in range(N):
            if i <= reach:
                reach = max(reach, i + nums[i])
                if reach >= N - 1:
                    return True
            else:
                return False
        
