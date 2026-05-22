class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = [0] * (n + m)

        i, j, k = 0, 0, 0

        while i < n and j < m:
            if k % 2 == 0:
                res[k] = word1[i]
                i += 1
                k += 1
            else:
                res[k] = word2[j]
                j += 1
                k += 1
        
        
        while i < n:
            res[k] = word1[i]
            i += 1
            k += 1
        
        while j < m:
            res[k] = word2[j]
            j += 1
            k +=1 

        return "".join(res)

    
