class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        Total = sum(piles)

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            even = True if (r - l) % 2 == 0 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(left + dfs(l+1, r),
                        right + dfs(l, r-1))
            return dp[(l, r)]
        
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > Total - alice_score

        
