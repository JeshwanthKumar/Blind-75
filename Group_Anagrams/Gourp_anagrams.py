#Time_Complexity: O(n(l*l log l))
#Space_Complexity: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= {}     #Initialize a hashmap
        result = []     #Initialize a result array
        
        for word in strs:   #Loop over all of the strings in array 
            key = sorted(word)  #Initialize a key with the sorted word
            key="".join(key)    #Join the sorted splitted and sorted word
            if key not in hashmap:  #If the key is not in the hashmap then add the word to the hashmap
                hashmap[key] = [word]
                
            else:   #Else append the word into the hashmap[key]
                hashmap[key].append(word)
                
        for k, v in hashmap.items():    #For every keys and values in the hashmap append the values to the result array
            result.append(v)
        
        return result   #Return result array