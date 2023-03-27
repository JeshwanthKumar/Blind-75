# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.treeFlag = False
        self.dfs(root, subRoot)
        return self.treeFlag


    def dfs(self, root, subRoot):
        if root == None:
            return

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

        if not self.treeFlag and root.val == subRoot.val:
            self.treeFlag = self.isSameTree(root, subRoot)
            return
            

    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        
        if p == None and q or p and q == None:
            return False
        
        if p.val != q.val:
            return False
        

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
