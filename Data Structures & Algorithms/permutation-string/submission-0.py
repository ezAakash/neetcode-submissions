from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        check = len(c) # tells me number of unique character
        S1_LEN = len(s1)
        l = 0

        for r in range(len(s2)):
            if s2[r] in c:
                c[s2[r]] -= 1
                if c[s2[r]] == 0:
                    check -= 1
            
            if r - l + 1 == S1_LEN:
                if check == 0:
                    return True
                else:
                    if s2[l] in c:
                        if c[s2[l]] == 0:
                            check += 1
                        c[s2[l]] += 1
                    l +=1 

        return False 

