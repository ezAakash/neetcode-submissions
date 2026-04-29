class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
         
        def solve(i : int, sum: int):
            if target == sum:
                res.append(subset.copy())
                return 
            if i >= len(nums) or sum > target:
                return 

            for j in range(i, len(nums)):
                subset.append(nums[j])
                solve(j, sum + nums[j])
                subset.pop()
        
        solve(0, 0)
        return res