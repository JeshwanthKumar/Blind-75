# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:    #If root is None then return empty string
            return ""
        result = [] #Initialize result as an empty array
        q = deque() #Initialize queuse as q using deque
        q.append(root)  #Append root into the q

        while q:    #Continue till the q is not empty
            node = q.popleft()  #Pop the first element in the q using popleft and store it in node
            if node:    #If node is not empty
                q.append(node.left) #Append node.left into q
                q.append(node.right)    #Append node.right into q
                result.append(str(node.val))    #Append node.val into result as a string
            else:
                result.append("null")   #Else append "null" to result, which means there is no node


        return ",".join(result) #Join and return result using "," as a delimitter
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:    #If there is no data return None
            return None
        data = data.split(",")  #Split the data using "," as a delimitter
        i = 0   #Initialize i as 0
        q = deque() #Initialize queue using deque
        root = TreeNode(int(data[0]))   #Initialize root as TreeNode with first element of data by converting it into integer
        q.append(root)  #Append root into q
        i+=1    #Increment i by 1
        while q:    #Continue till q is not empty
            node = q.popleft()  #Pop the first lement in the q using popleft and store it in node
            #Processing for left side of the tree
            if data[i] != "null": #If data[i] is not equal to "null"
                node.left = TreeNode(int(data[i]))  #Then intialize node.left as Treenode with data[i] as value by converting it into integer
                q.append(node.left) #Append node.left into q
            i+=1    #Incerment i by 1

            #right
            if data[i] != "null": #If data[i] is not equal to "null"
                node.right = TreeNode(int(data[i])) #Then intialize node.left as Treenode with data[i] as value by converting it into integer
                q.append(node.right)    #Append node.right into q
            i+=1    #Incerment i by 1

        return root #Return root wihch will give the Tree
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))