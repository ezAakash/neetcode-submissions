class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def isValid(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                
                if cnt == p:
                    return True
            
            return False

                    

        nums.sort()
        l, r = 0, abs(nums[-1] - nums[0])
        while l < r:
            mid = l + (r - l) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
