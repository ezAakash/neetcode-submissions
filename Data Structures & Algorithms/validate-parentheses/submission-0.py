class Solution:
    def isValid(self, s: str) -> bool:
        #here again we need to keep mind of what came earlier.
        stack = []
        map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for c in s:
            if c in ['[','(','{']:
                stack.append(c)
            else:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack) == 0
