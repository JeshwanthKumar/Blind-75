#time_Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #Initialize an hashset to store the elements in the array
        for i in nums:  #Continue till nums
            if i in hashset:    #If the element is already present in hashset then return True, it means the array has duplicates
                return True
            hashset.add(i)  #Else add it to the hashset
        return False    #Finally return False, it means there is no duplicates in the arrray