#Time_Complexity: O(nlogk)
#Space_Complexity: O(k) - It depends on k

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [] #Initialize a heap as hq
        
        for num in nums:    #Conitinue till nums
            heappush(hq, num)   #Push num into hq by using heappush
            if len(hq) > k: #If the length of hq is greater than k
                heappop(hq) #Pop the last element in the hq
                
        return hq[0]    #Return the first element in the heap hq