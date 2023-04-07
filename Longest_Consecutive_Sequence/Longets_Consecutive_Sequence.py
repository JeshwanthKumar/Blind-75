class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  #Put all the elements in a set as numSet
        result = 0  #Initialize resutl as 0
        for n in nums:  #Continue till nums
            if (n-1) not in numSet: #If n-1 which is the element is not in numSet then
                length = 1  #Initialize length by 1
                while (n+length) in numSet: #Continue till n+legnth is in numSet
                    length +=1  #Increment length by 1
                result = max(length,result) #Change result by checkign max between legnth and result
        return result   #Return result which will give the longest sequence