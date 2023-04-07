class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) #Initialize m as the legnth of rows
        n = len(matrix[0])  #Initialize n as the length of columns
        
        rowSet = [False]*m  #Initialize rowSet as False for m size
        colSet = [False]*n  #Initialize colSet as False for n size

        for i in range(m):  #Continue till m
            for j in range(n):  #Continue till n
                if matrix[i][j] == 0:   #If matrix[i][j] is equal to 0 
                    rowSet[i] = True    #then change rowSet fo that row to True
                    colSet[j] = True    #Change colSet of that column to True
    #This will hold the 0s in the matrix
            if rowSet[i]:   #If rowSet[i] is True
                matrix[i] = [0] * n #Change all the values in that row to 0

        for i in range(m):  #Continue till m
            if rowSet[i]:   #If the rowSet[i] is true then continue
                continue
            for j in range(n):  #Continue till n
                if colSet[j]:   #If colSet[j] is True
                    matrix[i][j] = 0    #Change all the elements in that column to 0