class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr_sum = [], []
        def solve(i, sum):
            if target == sum:
                res.append(curr_sum.copy())
                return

            if sum > target:
                return 

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                

                curr_sum.append(candidates[j])
                solve(j+1, sum + candidates[j])
                curr_sum.pop()

        solve(0, 0)
        return res