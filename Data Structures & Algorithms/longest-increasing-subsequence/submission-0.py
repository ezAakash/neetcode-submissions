class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def solve(i: int, prev: int):
            if i == len(nums):
                return 0

            choose = 0
            if prev == None or prev < nums[i]:
                choose = 1 + solve(i+1, nums[i])

            skip = solve(i+1, prev) 

            return max(choose, skip)

        return solve(0, None)