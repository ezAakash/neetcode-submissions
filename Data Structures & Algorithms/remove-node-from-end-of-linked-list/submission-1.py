# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1 
            curr = curr.next 
        
        pos_fr_start = size - n

        i = 0
        prev, curr = None, head
        while i < pos_fr_start:
            prev = curr
            curr = curr.next 
            i += 1
        
        if prev != None: # that means we got size == n 
            prev.next = curr.next
            return head
        
        return head.next

        








