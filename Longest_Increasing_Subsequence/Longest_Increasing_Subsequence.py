#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)   #Initialize n to store the length of nums
        dp =[1]*n   #Initialize an array full of 1s for the length of n as dp
        #THIS IS FOR THE FOLLOW-UP QUESTION
        dp2 = [[] for _ in range(n)]    #Initialize dp2 that captures all the elements in that instance as array of arrays
        for i in range(n):  #Continue till n
            dp2[i] = [nums[i]]  #Insert the elements into the dp2 array
            for j in range(i):  #Continue till i
                if (nums[i] > nums[j]): #If the nums[i] is greater than nums[j]
                    if dp[j]+1 > dp[i]: #If the dp[j+1] is greater than dp[i]
                        dp[i] = dp[j]+1 #Then change the dp[i] as dp[j]+1
                        #dp2[i] = dp2[j]+[nums[i]] 

        #print(dp2) #By printing dp2 we get all the subsequences that's been formed
        return max(dp)  #By returning max(dp) it gives the length of the longest subsequence