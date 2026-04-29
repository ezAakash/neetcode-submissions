class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(i: int, curr: List[int]):
            if i == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[i]) 
            solve(i+1, curr)
            curr.pop()
            solve(i+1, curr)


        solve(0, [])
        return res