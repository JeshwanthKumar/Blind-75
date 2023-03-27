# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.smallest = root.val
        self.k = k
        self.dfs(root)
        return self.smallest

    def dfs(self, root):
        if root == None or self.k <= 0:
            return

        self.dfs(root.left)

        self.k -= 1
        if self.k == 0: self.smallest = root.val

        self.dfs(root.right)