# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()   #Initialize a dummy node as prev to carry out the reference
        curr = prev #Initialize curr to prev

        while list1 and list2:  #Continue the loop untill either list1 or list2 is None
            if list1.val < list2.val:   #If the value of list is less than the value of list2 change curr.next to list1
                curr.next = list1
                curr = list1    #Change curr to list1
                list1 = list1.next  #Change list1 to list1.next
            else:   #Else change curr.next = list2
                curr.next = list2   
                curr = list2    #Change curr to list2
                list2 = list2.next  #Change list2 to list2.next

        if list1:   #If list1 is not None change curr.next to listq1
            curr.next = list1
        if list2:   #If list2 is not None change curr.next to list2
            curr.next = list2

        return prev.next    #Return prev.next which will give the head of the linked list