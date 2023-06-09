# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.dfs(root, 1)
        return self.maxDepth
        
    def dfs(self, root, depth):
        if root == None:
            return

        self.maxDepth = max(depth, self.maxDepth)

        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)