# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: #Check if preorder and inorder are not None, if yes, then return None
            return None

        root = TreeNode(preorder[0])    #Initialize root as TreeNode with first element of preorder as value

        for i in range(len(inorder)):   #Continue till length of inorder
            if inorder[i] == preorder[0]:   #If inorder[i] is equal to first element of preorder 
                pivot = i   #Then intialize pivot as i

        root.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot]) #Initialize root.left by recursively calling buildTree of preorder from 1 to pivot+1 and inorder from 0 to pivot
        root.right = self.buildTree(preorder[pivot+1:],inorder[pivot+1:])   #Initialize root.right by recursively calling buildTree of preorder from pivot+1 to end of preorder and inorder from pivot+1 to end of inorder

        return root #Return root which will give the tree