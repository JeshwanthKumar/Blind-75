#Time_Complexity: O(logn)
#Space_Compelxity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        low=0   #Initialize low as 0
        high=len(s)-1   #Initialize high to the last elemtn

        while low<high: #Conitune till low is less than high
            if not s[low].isalnum():    #If s[low] is no alphanumeric
                low+=1  #Increment low by 1 and continue
                continue
            if not s[high].isalnum():   #If s[high] is not alphanumerc
                high-=1 #Decrement high by 1 and contune
                continue
            if s[low].lower()!=s[high].lower(): #IF s[low].lower is not equal to s[high].lower
                return False    #Retuen False
            
            low+=1  #Increment low by 1
            high-=1 #Decrement high by1

        return True #Return true, it means the given string is palindrome