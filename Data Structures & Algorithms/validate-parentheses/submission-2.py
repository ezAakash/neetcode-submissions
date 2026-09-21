class Solution:
    def isValid(self, s: str) -> bool:
        #here again we need to keep mind of what came earlier.
        stack = []
        closeToOpen = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
        
