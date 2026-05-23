class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, num in enumerate(nums):
            if num not in map:
                map[num] = i
                continue
            
            if abs(map[num] - i) <= k:
                return True
            else:
                map[num] = i
        
        return False