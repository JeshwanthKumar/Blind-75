# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space O(n)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = []    #Initialize a result array
        self.inorder(root)  #Recursion
        
        for i in range(1, len(self.result)):    #Continue till the length of the result array
            if self.result[i-1] < self.result[i]:   #If the previous value is less than the current value then continue
                continue
            else:   #Else return false because the values are not in sorted order which violates the validate binary seach tree constraint
                return False
            
        return True #If everything passes return True
        
    def inorder(self, root):    #Recursive function
        
        #base condition
        if root == None:    #If the root is none then return which unfolds the recursion 
            return
        
        self.inorder(root.left) #Recursive call for the left side of the tree
        self.result.append(root.val)    #Append the value into the result array
        
        self.inorder(root.right)    #Recursive call for the right side of the tree
        