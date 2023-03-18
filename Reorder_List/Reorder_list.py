# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findMid(head)
        midNext = mid.next
        mid.next = None
        headB = self.reverse(midNext)
        headA = head
        
        self.merge(headA, headB)
        
        
    def findMid(self,head):
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
    def reverse(self,head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def merge(self,head1, head2):
        p1 = head1
        p2 = head2
        
        while p2:
            temp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp
        
        