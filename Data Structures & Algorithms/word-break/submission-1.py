class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]
                
            for w in wordDict:
                if s.startswith(w):
                    remain_word = s[len(w):]

                    if dfs(remain_word):
                        memo[s] = True
                        return memo[s]
            
            memo[s] = False
            return memo[s]

        
        return dfs(s)