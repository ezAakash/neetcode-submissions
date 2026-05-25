class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        c = Counter(t)
        c_size = len(c)

        l = 0

        min_len = float('inf')
        start = 0

        r_map = {}#needed because we want to check is the till now substrings covered all the required characters or not
        r_size = 0 # this is for once , we have the atleast minimum no. of unique required characters.
    
        for r in range(len(s)):
            if s[r] in c:
                r_map[s[r]] = 1 + r_map.get(s[r],0) 
                if c[s[r]] == r_map[s[r]]:
                    r_size += 1 

            while c_size == r_size:# ye barabar tab honge jab exist krte hoh.
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                
                if s[l] in r_map:
                    r_map[s[l]] -= 1
                    if c[s[l]] > r_map[s[l]]:
                        r_size -= 1
                l += 1

        return s[start:start+min_len] if min_len != float('inf') else ""


