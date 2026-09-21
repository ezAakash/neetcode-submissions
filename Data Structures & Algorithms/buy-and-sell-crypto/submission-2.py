class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0

        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                maxProfit = max(maxProfit, profit)
        
        return maxProfit
            