class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resInd = 0
        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if(R - L + 1 > resLen):
                    resLen = R - L + 1
                    resIn = L
                L -= 1
                R += 1
            
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if(R - L + 1 > resLen):
                    resLen = R - L + 1
                    resIn = L
                L -= 1
                R += 1
        
        return s[resIn : resIn + resLen]