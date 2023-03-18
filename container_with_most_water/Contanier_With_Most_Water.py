#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1   #Initialize n to the length of height-1
        first = 0   #Initialize the first pointer to 0
        last = n    #Initialize the last pointer to n
        
        max_area = 0    #Initialize the max_area to 0
        
        while first <= last:    #Continue till fast and last crosses each other
            max_area = max(max_area, (min(height[first],height[last])*(last-first)))    #Store the maximum between max_area and the minimum between height[first] and height[last] and multiply tha while thing with the difference of last and first
             
            if height[first] < height[last]:    #If the heaight of first is less than the height of last increment first
                first+=1
            else:   #Else decrement last
                last-=1
                
                
        return max_area #Return the max_area