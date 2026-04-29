class Solution:
    def numDecodings(self, s: str) -> int:

        def solve(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = 0
            res += solve(i+1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += solve(i+2)  

            return res

        def solvedp():
            dp = [0] * (len(s) + 1) 

        return solve(0)

