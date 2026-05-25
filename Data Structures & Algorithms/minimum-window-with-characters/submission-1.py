class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freqT = Counter(t)
        lenT = len(freqT)

        reqS = {}
        lenS = 0

        l, start = 0, 0
        res = float('inf')

        for r in range(len(s)):
            if s[r] in freqT:
                reqS[s[r]] = 1 + reqS.get(s[r], 0)

                if reqS[s[r]] == freqT[s[r]]:
                    lenS += 1

            
            while lenT == lenS:
                if r - l + 1 < res:
                    res = r - l + 1
                    start = l
                
                if s[l] in reqS:
                    reqS[s[l]] -= 1

                    if reqS[s[l]] < freqT[s[l]]:
                        lenS -= 1
                
                l += 1
            
        return s[start: start + res] if res != float('inf') else ""

                


        
                



            


