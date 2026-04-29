class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxm = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr) # naya banau ya purana follow karu
            maxm = max(curr, maxm)

        return maxm