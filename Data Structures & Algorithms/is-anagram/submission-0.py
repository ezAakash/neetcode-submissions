class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        freq_s = [0] * 26
        freq_t = [0] * 26

        for cs, cr in zip(s, t):
            freq_s[ord(cs) - ord('a')] += 1
            freq_t[ord(cr) - ord('a')] += 1
        
        for i in range(26):
            if freq_s[i] != freq_t[i]:
                return False

        return True

            