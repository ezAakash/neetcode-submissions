class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def solve(i: int, path: List[int]):
            res.append(path.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                solve(j+1, path)
                path.pop()
            
        solve(0, [])
        return res