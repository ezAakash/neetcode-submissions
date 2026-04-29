class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr_sum = [], []
        def solve(i, sum):
            if target == sum:
                res.append(curr_sum.copy())
                return
            
            if i >= len(candidates) or sum > target :
                return 

            # atleast one or more same candidate
            curr_sum.append(candidates[i])
            solve(i+1, sum + candidates[i])
            curr_sum.pop()
            # skip all of the same 
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1 
            solve(i+1, sum)

        solve(0, 0)
        return res