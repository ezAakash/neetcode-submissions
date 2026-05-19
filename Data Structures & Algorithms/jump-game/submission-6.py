class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)

        reach = 0

        for i in range(N):
            if i <= reach:
                reach = max(reach, i + nums[i])
            else:
                return False
        
        return True
        
