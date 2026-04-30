class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      
        def dp():
            dp1 = [False] * (len(s) + 1)

            dp1[-1] = True

            for i in range(len(dp1) - 2, -1, -1):
                for word in wordDict:
                    if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                        if dp1[i+len(word)]:
                            dp1[i] = True
            
            return dp1[0]

        return dp()