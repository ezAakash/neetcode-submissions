class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
         
        def solve(i : int, sum: int):
            if target == sum:
                res.append(subset.copy())
                return 

            if i == len(nums):
                return 

            if sum + nums[i] <= target:
                subset.append(nums[i])
                solve(i, sum + nums[i])
                subset.pop()

            solve(i+1, sum)

        solve(0, 0)
        return res