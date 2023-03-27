class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        zigzag = False
        result = [[root.val]]

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)

            if level:
                if zigzag:
                    result.append(level)
                else:
                    level.reverse()
                    result.append(level)
            zigzag = not zigzag

        return result