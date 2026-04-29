class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_m = min(nums)
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sub_pro = 1
                x, y = i, j
                while (x <= y):
                    curr_sub_pro *= nums[x]
                    x += 1

                max_m = max(max_m, curr_sub_pro)
                curr_sub_pro = 1
        return max_m