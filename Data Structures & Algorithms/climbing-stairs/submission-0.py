class Solution:
    def climbStairs(self, stairs: int) -> int:
        
        def solve(i: int):
            if i > stairs:
                return 0
            if i == stairs:
                return 1
            
            return solve(i+1) + solve(i+2)
        
        return solve(0) #here i am defining the starting point .