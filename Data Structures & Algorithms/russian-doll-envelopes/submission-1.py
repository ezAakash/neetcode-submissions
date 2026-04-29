class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],x[1]), reverse= True)
        print(envelopes)

        n = len(envelopes)
        dp = [1] * (n) 
        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
      
        print(dp)
        return max(dp)
                


