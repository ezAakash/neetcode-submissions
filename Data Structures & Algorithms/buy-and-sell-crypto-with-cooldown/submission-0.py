class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, prevBought):
            if i >= n:
                return 0

            if prevBought >= prices[i]:
                #buy
                return dfs(i+1, prices[i])
            else:
                #sell
                profit = prices[i] - prevBought 
                return max(profit + dfs(i+2, float('inf')), dfs(i+1, prevBought))
        
        return dfs(0, float('inf'))