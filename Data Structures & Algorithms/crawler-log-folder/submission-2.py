class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        cnt_depth = 0 #standing at root 
        for log in logs:
            if log == '../':
                cnt_depth = max(0, cnt_depth - 1)
            elif log == './':
                continue
            else:
                cnt_depth += 1

        return cnt_depth

        