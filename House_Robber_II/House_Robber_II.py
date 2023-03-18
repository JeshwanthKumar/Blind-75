#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
       if len(nums) == 1:   #If len(nums) is equal to 1 return first element of nums
            return nums[0]
       if len(nums) == 2:   #If len(nums) is equal to 2 return max between nums[0] and nums[1]
            return max(nums[0], nums[1])
        
       return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))   #Return ,ax between nums[0] and helper function from(nums[1:] and nums[:-1])


    def helper(self, nums): #Another function as helper
        dp = [] #Initialize an empty array as dp
        
        if (len(nums) >= 1):    #If len(nums) >= 1 then append that element into the dp array
            dp.append(nums[0])
        if (len(nums) > 1): #If the len(nums) is greater than 1 append that value value by checking the maximum between nums[0] and nums[1]
            dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):   #Continue the loop from second index to the length of the array
            dp.append(max((nums[i] + dp[i - 2]), dp[i - 1]))    #Append the values into dp array by checking the maximum between nums[i] +dp[i-2] and dp[i-1]

        return dp[-1]   #Return the last element in dp that will give the maxProfit from the houese robbed