class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt_palindromes = 0
        for i in range(len(s)):
            l, r = i, i #odd length unique

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt_palindromes += 1
                l -= 1
                r += 1

            l, r = i, i + 1 #even length unique

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt_palindromes += 1
                l -= 1
                r += 1

        return cnt_palindromes

            