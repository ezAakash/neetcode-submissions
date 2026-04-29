class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0) + 1
        
        for num in nums:
            if map[num] == 1:
                return num
        
        
        
