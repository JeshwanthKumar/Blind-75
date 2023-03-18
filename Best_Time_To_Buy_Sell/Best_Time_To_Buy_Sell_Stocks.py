#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0   #Initialize l as 0
        r = 1   #Initialize r as 1
        maxProfit = 0   #Initialize maxProfit as 0

        while r<len(prices):    #Continue till r is less than the length of prices arrat
            if prices[r] > prices[l]:   #If the prices[l] is lesser thant the prices[r]
                maxProfit = max(maxProfit, (prices[r] - prices[l])) #Change the maxProfit with max between maxProfit and the difference between price[r] and price[l]
            else:
                l = r   #Else change l to r
            r+=1    #Increment r by 1
        return maxProfit    #Return maxProfit in the array