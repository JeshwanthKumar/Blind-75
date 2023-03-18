#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d = len(nums)-1 #Initialize d to store the length of nums

        for i in range(len(nums)-2,-1,-1):  #Run the loop from n-2 to 0 in reverse
            if i + nums[i] >=d: #If the addition of the index and nums[i] is less than or equal to d
                d = i   #Then change d to i

        return d == 0   #Finally return d as 0