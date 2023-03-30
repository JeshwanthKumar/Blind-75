class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []   #If there is no root return an emoty array

        q = deque() #Initialize a 1 using deque
        q.append(root)  #Append the root into the q
        zigzag = False  #Set zigzag as False, which acts aas a flag
        result = [[root.val]]   #Insert root.val as an array of arrays in result array

        while q:    #Continue till q is not empty
            size = len(q)   #Initialize size as lenght of q, it measn there are size elements in that level and the loop runs for size times
            level = []  #Initiailze a level array

            for _ in range(size):   #Continue till size
                node = q.popleft()  #Pop the first element in q and store it as node
                
                if node.left:   #If nide.left exists append node.left into the q and append node.left.val into level
                    q.append(node.left)
                    level.append(node.left.val)
                if node.right:  #If node.right exists append node.right into the q and append node.left into level
                    q.append(node.right)
                    level.append(node.right.val)

            if level:   #If level is not None
                if zigzag:  #If zigzag is not None
                    result.append(level)    #Append level intop the result
                else:
                    level.reverse() #Else reverse the level
                    result.append(level)    #And append it to the result
            zigzag = not zigzag #Change the flag

        return result
