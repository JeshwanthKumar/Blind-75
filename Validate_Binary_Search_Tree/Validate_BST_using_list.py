# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Compolexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        stack = []
        node = root
        prev = float('-inf')
        while stack or node:

            if node:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                node = node.right
       
        return True