class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i, j):
            k = i+j
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            ans = False
            if i < len(s1) and s3[k] == s1[i]:
                ans |= dfs(i+1, j)
            if j < len(s2) and s3[k] == s2[j]:
                ans |= dfs(i, j+1)

            memo[(i, j)] = ans
            return ans
                
        return dfs(0, 0)