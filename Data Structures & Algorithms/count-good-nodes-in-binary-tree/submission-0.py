# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, min_path_val):
            if not root:
                return

            if root.val >= min_path_val:
                self.count += 1

            dfs(root.left, max(root.val, min_path_val))
            dfs(root.right, max(root.val, min_path_val))
        
        dfs(root, root.val)

        return self.count