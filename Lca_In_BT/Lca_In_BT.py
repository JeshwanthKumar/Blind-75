class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p=p
        self.q=q
        return self.dfs(root,p,q)
    def dfs(self,root,p,q):
        if not root:
            return
        if root.val==p.val or root.val==q.val:
            return root
        left=self.dfs(root.left,p,q)
        right=self.dfs(root.right,p,q)
        if left and right:
            return root
        else:
            return left or right