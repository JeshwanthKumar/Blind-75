class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        direction = 1
        result = []

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            level= level[::direction]
            direction*=-1
            result.append(level)
            

        return result