#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMinimum = nums[0]    #Initialize currentMinimum as the first element of nums
        currentMaximum = nums[0]    #Initialize currentMaximum as the first element of nums
        globalMaximum = nums[0]     #Initialize globalMaximum as the first element of nums

        start = 0   #Initialize start as 0
        end = 1 #Initialize end as 1

        for i in range(1,len(nums)):    #Continue the loop till the end of nums
            currentMinimum, currentMaximum  = min(currentMinimum * nums[i], currentMaximum * nums[i], nums[i]), max(currentMinimum * nums[i], currentMaximum * nums[i], nums[i])
            #Swap the currentMin and currentMax with min(currentMinimum * nums[i], currentMaximum * nums[i], nums[i]), max(currentMinimum * nums[i], currentMaximum * nums[i], nums[i])
            if (currentMaximum > globalMaximum):    #If the currentMax is greater than globalMax then change globalMax as currentMax
                globalMaximum = currentMaximum
                end=i+1 #Increment end by the index+1
                

        j=end-1 #Initialize j as end-1
        while j>=0: #Continue till j is greater than 0
            if nums[j]==0:  #If nums[j] is equal to 0 change start to j and break
                start = j
                break
            else:   #Else if globalMax is equal to nums[j] then change start as j and break
                if globalMaximum == nums[j]:
                    start = j
                    break
                globalMaximum = globalMaximum/nums[j]   #Change globalMaximum to globalMax/nums[j] to get the index of the element where the globalMax is changed to get the starting of the pair
            j-=1    #Decrement j by 1

        #nums[start: end] is the maximum product subarray!!
        prod = 1    #Initialize prod as 1
        for num in nums[start: end]:    #Continue till num in nums[start:end]
            prod *=num  #Multiply prod with num
        #THIS IS FOR THE FOLLOW-UP QUESTION, IF THEY ASK WHAT ARE THE PAIRS THAT CONTRIBUTED TO FIND THE MAXPRODUCT
        print(start, end-1) #By printing the start and end, it gives the pairs that contributed to the maximum product
        return prod #Retrun prod to get the maxProd