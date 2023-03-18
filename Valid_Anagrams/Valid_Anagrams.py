#Time_Complexity: O(n)
#Space_Complexity: O(26) -> O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):  #If the lenght of s is not equal to the length of t return False, it meanse they both cannot be anagrams
            return False
        bucket=[0]*26   #Initialize bucket with length of 26 filled with 0s

        for ch in s:    #Continue till the characters in s
            bucket[ord(ch)-ord("a")]+=1 #Add 1 to the char by subtracting that character with ASCII value of 'a' which gives the index of that char
        for ch in t:    #Continue till the characters in t
            bucket[ord(ch)-ord("a")]-=1 #Subtract 1 to the char by subtracting that character with ASCII value of 'a' which gives the index of that char
            if bucket[ord(ch)-ord('a')] < 0:    #If any of the valuse in bucket is greater of less than 0 then return False
                return False
        
        return True #Return true, it means s and t are anagrams to each other