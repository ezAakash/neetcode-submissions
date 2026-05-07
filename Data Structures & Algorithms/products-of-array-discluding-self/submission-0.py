class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        multi = 1
        for i in range(1, len(nums)):
            multi *= nums[i-1]
            prefix[i] = multi
        
        multi = 1
        for i in range(len(nums) - 2, -1, -1):
            multi *= nums[i+1]
            suffix[i] = multi
        
        res = [] 
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res
        