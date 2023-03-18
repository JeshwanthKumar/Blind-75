#Time_Complexity: O(n)
#Space_Complexity: O(6) -> O(1)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: #If the length of is not divisible by 2 then return False, which means no valid paranthesis
            return False

        hashmap= { '}':'{', ']':'[', ')':'('}   #Initialize hashmap with all the closing paranthesis as key and open paranthesis as values
        stack = []  #Initialize an empty stack to store the paranthesis

        for ch in s:    #Continue till character in s
            if ch in hashmap:   #If the ch is in hashmap
                if stack and stack[-1]==hashmap[ch]:    #If stack is not empty and last element in stack is queal to hashmap of that ch
                    stack.pop() #Pop the last element in stack
                else:   #Else return False
                    return False

            else:   #Else append that ch in stack
                stack.append(ch)

        return len(stack)==0    #Return True if length of stack is 0