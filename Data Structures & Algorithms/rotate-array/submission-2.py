class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i = len(nums) - k
        leftPart = nums[:i]
        rightPart = nums[i:]

        nums[:] = rightPart + leftPart
        print(nums)