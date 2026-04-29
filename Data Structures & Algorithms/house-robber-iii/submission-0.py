# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}

        def dfs(node):
            #base case 
            if node == None: 
                return 0
            
            if node in memo:
                return memo[node]

            skip = dfs(node.left) + dfs(node.right)

            take = node.val
            if node.left != None:
                take += dfs(node.left.left) + dfs(node.left.right)
            
            if node.right != None:
                take += dfs(node.right.left) + dfs(node.right.right)
            

            memo[node] = max(take, skip)
            return memo[node]
        
        return dfs(root)