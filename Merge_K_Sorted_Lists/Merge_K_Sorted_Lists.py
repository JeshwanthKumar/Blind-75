# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Time_Complexity: O(nlogk)
#Space_Complexity: O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda a,b : a.val < b.val    #Using lesser than "lt" operator comparing the value of two List nodes
        minHeap = []    #Intialize minHeap as an array
        
        result = ListNode(-1)   #Initialize result as a ListNode with -1 as a dummy node
        curr = result   #Initiailze curr as result
        
        for lHead in lists: #For lHead in lists
            if lHead:   #If lHead is True
                heappush(minHeap, lHead)    #Push lHead into the minHeao using heappush
        while minHeap:  #Continue till minHeap is True
            top = heappop(minHeap)  #Initialize top as the last element popped out of minHeap
            curr.next = top #Change curr.next as top
            curr = curr.next    #Change curr as curr.next
            if top.next:    #If top.next is True
                heappush(minHeap, top.next) #Push top.ext into minHeap using heappush
                
        return result.next  #Return result.next