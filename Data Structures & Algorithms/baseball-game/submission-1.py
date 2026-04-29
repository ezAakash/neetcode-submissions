class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # needed to recall what come earlier 
        # some postfix style : stack 
        stack = []
        for oper in operations:
            if oper == '+':
                last, lastTolast = stack[-1], stack[-2]
                stack.append(last + lastTolast)
            elif oper == 'D':
                stack.append(stack[-1] * 2)
            elif oper == 'C':
                    stack.pop()
            else:
                stack.append(int(oper))
        return sum(stack)
    
