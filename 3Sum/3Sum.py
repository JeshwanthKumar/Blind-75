#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)   #Initialize n as length of nums
        triplets = []   #Initialize an empty array as triplets
        nums.sort() #Sort the nums
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:  #If the i > 0 and nums[i] == nums[i-1] then continue
                continue
                
            p1= i+1 #Initialize p1 pointer to i+1
            p2= n-1 #Initialize p2 pointer to n-1
            target = 0- nums[i] #Initialize target as the difference between 0 and nums[i]
            
            while p1< p2:   #Continue till p1 and p2 crosses each other
                if nums[p1]+nums[p2] == target: #If nums[p1]+nums[p2] is equal to target store nums[i], nums[p1], nums[p2] into the triplet array
                    result = [nums[i], nums[p1], nums[p2]]
                    triplets.append(result)
                    while p1<p2 and nums[p1] == nums[p1+1]: #Continue till p1 corsses p2 and nums[p1] is equal to nums[p1+1]
                        p1+=1   #Increment p1 by 1
                        
                    while p1<p2 and nums[p2] == nums[p2-1]: #Continue till p1 corsses p2 and nums[p2] is equal to nums[p2-1]
                        p2-=1   #Decrement p2 by 1
                    p1+=1   #Increment p1 by 1
                    p2-=1   #Decrement p2 by 1
                else:   #Else if the target is less than nums[p1]+nums[p2] decrement p2 by 1
                    if target < nums[p1]+nums[p2]:
                        p2-=1
                        
                    else:   #Else increment p1 by 1
                        p1+=1
                        
        return triplets  #Return triplets