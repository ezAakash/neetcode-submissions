class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        suffix = [0] * len(piles)
        suffix[-1] = piles[-1]
        for i in range(len(piles) - 2, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        
        dp = {}
        def dfs(i, M):
            if i >= len(piles):
                return 0
            
            if i + 2 * M >= len(piles):
                return suffix[i]
            
            if (i, M) in dp:
                return dp[(i, M)]
            res = float('-inf')
            for X in range(1, 2*M + 1):
                if i + X > len(piles):
                    break
                
                gain = (suffix[i] - suffix[i+X])

                res = max(res, gain - dfs(i+X, max(X, M)))

            dp[(i, M)] = res
            return res
            
        diff = dfs(0, 1)
        return (suffix[0] + diff) // 2
            
