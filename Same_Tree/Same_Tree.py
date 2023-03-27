# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        pPath = []
        qPath = []
        
        self.dfs(p, pPath)
        self.dfs(q, qPath)
        
        return pPath == qPath
            
        
    def dfs(self, root, path):
        if root:
            path.append(root.val)
        
            self.dfs(root.left,path)
            
            
            self.dfs(root.right,path)
        else:
            path.append(None)
        