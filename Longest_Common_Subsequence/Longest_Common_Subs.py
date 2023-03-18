#Time_Complexity: O(len(text1)) or O(len(text2))
#Space_Complexity: O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) #m is the length of text1
        n = len(text2) #n is the length of text2
        grid = [[0 for i in range(n+1)] for j in range(m+1)] #Initialize grid with 0s for n+1 and m+1

        for i in range(m-1,-1,-1):  #Traverse in reverse through the grid from m-1
            for j in range(n-1,-1,-1):  #Traverse in ereverse through the grid from n-1
                if text1[i]==text2[j]:  #If text[i] is equal to text[j]
                    grid[i][j] = 1+ grid[i+1][j+1]  #Add 1 to that element in the grid

                else:
                    grid[i][j] += max(grid[i][j+1],grid[i+1][j]) #Else add that element in that grid with the maximum between grid[i][j+1] and grid[i+1][j]

        return grid[0][0] #Return the first element in the grid
        