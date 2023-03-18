# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Time_Complexity: O(n)
#Space_Complexity: O(1)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0   #Initialize count to 0
        dummy = ListNode(0, head)   #Initialize a dummy node as the start of the linked list
        slow = dummy    #Initialize slow to dummy's position
        fast = dummy    #Initialize fast to dummy's position
        while count < n:    #Continue till the count becomes n
            fast = fast.next    #Increment fast to fast.next
            count+=1    #Increment count to 1
            
        while fast.next != None:    #Continue till the fast.next is not equal to None
            slow = slow.next    #Increment slow to slow.next
            fast = fast.next    #Increment fast to fast.next

        slow.next = slow.next.next  #Increment slow to slow.nex.tnext
        
        return dummy.next   #Return dummy.next which will give the actual linked list