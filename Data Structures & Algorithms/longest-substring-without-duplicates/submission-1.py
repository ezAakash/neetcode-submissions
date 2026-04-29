class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while r - l + 1 > len(count):
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            res = max(res, r - l + 1)

        return res