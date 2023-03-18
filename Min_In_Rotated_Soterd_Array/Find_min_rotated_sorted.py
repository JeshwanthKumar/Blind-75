#Time_Complexity: O(log n)
#Space_Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 #Initialize low to 0
        high = len(nums) -1 #Initialize high to lenght of nums-1
        if nums[low]<=nums[high]:
            return nums[low]    #If the given array is purely sorted then return the first element
        
        while low <= high:
            mid = low + (high-low) //2  #Integer overflow
            
            if nums[mid] > nums[mid +1]:    
                return nums[mid+1]  #If the next element to the middle is less than the middle then it is the minimum, return nums[mid+1]
            elif nums[low] <= nums[mid]:
                low = mid+1 #Else if nums[low] is less than the middle move the low to mid+1
            else:
                high = mid-1    #Else move the high to mid-1
                