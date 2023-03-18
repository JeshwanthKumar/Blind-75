# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None     #Initialize prev as None
        curr = head     #Initialize curr as head
        
        while curr:     #Continue till curr is not null
            temp = curr.next    #Initialize temp as curr.next
            curr.next = prev    #Change curr.next to prev
            prev = curr     #Change prev to curr
            curr = temp     #Change curr to temp
        return prev         #Return prev which is the head of the linked list