#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}    #Initialize a hashmap to store the pairs of sum
        
        for i in range(len(nums)):  #Continue till the end of nums array
            # diff = target - nums[i]
            
            if nums[i] in hashmap:  #If the element is in the hashmap return that index and the element in the hashmap
                return [i, hashmap[nums[i]]]
            hashmap[target - nums[i]] = i   #Set i as the index for hashmap[target-nums[i]]
            