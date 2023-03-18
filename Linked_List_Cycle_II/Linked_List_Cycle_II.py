# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Time_Complexity: O(n)
#Space_Complexity: O(1)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:    #If there is no head then return head
            return head
        
        slow = head     #Initialize slow as head
        fast = head     #Initialize fast as head
        cycle = False   #Initialize cycle as false
        
        while fast != None and fast.next != None:   #Continue till fast is not equal to None and fast.next is not equal to None
            slow = slow.next    #Increment slow to slow.next
            fast = fast.next.next   #Increment fast to fast.next.next 
            
            if slow == fast:    #If slow is equal to fast then there is a cycle in the linked list change cycle to True and break
                cycle = True
                break
                
        if not cycle:   #If there is no cycle return None
            return None
        
        slow = head     #Initialize slow as head
        
        while slow != fast: #Continue till slow is not equal to fast
            slow = slow.next    #Increment slow to slow.next
            fast = fast.next    #Increment fast to fast.next

        return slow     #Return slow which will give the position where the cycle started

        
        